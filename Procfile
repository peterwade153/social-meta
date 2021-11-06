release: python manage.py migrate --no-input
web: gunicorn app.wsgi:application --log-file -
worker: celery -A app worker -l info