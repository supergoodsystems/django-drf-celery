Steps:
1. clone this repo locally
2. set environment variables SUPERGOOD_CLIENT_ID and SUPERGOOD_CLIENT_SECRET (or pass them in manually within `settings.py`)
3. python -m venv venv
4. source venv/bin/activate
5. pip install supergood, Django, djangorestframework, django-celery-results, celery, Redis, sentry-sdk
6. Set your sentry DSN within `settings.py` (or comment out the sentry init if you dont want to test it)

set up a local redis backend:
`brew install redis
redis-server`

run the django server in one terminal:
`python manage.py migrate
python manage.py runserver`

run the celery worker in another terminal:
`cd examplesite
celery -A examplesite worker -l info`

You can test django-only calls using the `/my-ip` endpoint
You can test celery calls using the `/sum-my-ip` endpoint
