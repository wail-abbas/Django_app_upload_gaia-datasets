#!/bin/sh
until pg_isready -h db -p 5432 -U $POSTGRES_DB; do
    sleep 2
done

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD python manage.py createsuperuser --username $SUPERUSER_NAME --email $SUPERUSER_EMAIL --noinput


gunicorn core.wsgi:application --bind 0.0.0.0:8000

