import os
import requests
from datetime import datetime


class AbstractAPI:
    API_EMAIL_KEY = os.environ.get('ABSTRACT_EMAIL_API_KEY')
    API_IP_KEY = os.environ.get('ABSTRACT_IP_API_KEY')
    API_HOLIDAY_KEY = os.environ.get('ABSTRACT_HOLIDAY_API_KEY')

    def validate_email_format(self, email):
        url = f'https://emailvalidation.abstractapi.com/v1/?api_key={self.API_EMAIL_KEY}&email={email}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['is_valid_format']['value']

    def IPGeolocation(self):
        url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={self.API_IP_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['country_code']

    def country_holiday_today(self, country_code):
        today = datetime.today()
        year = today.year
        month = today.month
        day = today.day
        url = f'https://holidays.abstractapi.com/v1/?api_key={self.API_HOLIDAY_KEY}' + \
            f'&country={country_code}&year={year}&month={month}&day={day}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['name']
