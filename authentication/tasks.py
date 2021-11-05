import time
from requests.exceptions import Timeout, ConnectionError, HTTPError
from django.contrib.auth import get_user_model

from app.celery import app
from authentication.models import Holiday
from utils.abstract_api import AbstractAPI


User = get_user_model()
AbstractAPIClient =  AbstractAPI()

@app.task(bind=True)
def validate_user_email(self, email):
    time.sleep(1) # There is limit on the number of requests to Abstract api per second
    try:
        is_valid = AbstractAPIClient.validate_email_format(email=email)
        if is_valid:
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
    except (Timeout, ConnectionError, HTTPError) as exc:
        raise self.retry(exc=exc, countdown=30)

@app.task(bind=True)
def get_user_geolocation(self, email):
    time.sleep(1)
    try:
        country_code = AbstractAPIClient.IPGeolocation()
        user = User.objects.get(email=email)
        user.country_code = country_code
        user.save()
        return country_code
    except (Timeout, ConnectionError, HTTPError) as exc:
        raise self.retry(exc=exc, countdown=30)

@app.task(bind=True)
def update_user_geolocation_holiday(self, country_code):
    time.sleep(1)
    try:
        holiday = AbstractAPIClient.country_holiday_today(country_code)
        if holiday is not None:
            Holiday.objects.create(name=holiday, country_code=country_code) 
    except (Timeout, ConnectionError, HTTPError) as exc:
        raise self.retry(exc=exc, countdown=30)


def update_user_geo_data(email):
    chain = (get_user_geolocation.s(email) | update_user_geolocation_holiday.s())
    chain()
