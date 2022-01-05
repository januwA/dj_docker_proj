#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# daphne -b 0.0.0.0 -p ${DJANGO_PORT} proj.asgi:application
# python manage.py runserver 0.0.0.0:${DJANGO_PORT}
gunicorn -b 0.0.0.0:${DJANGO_PORT} proj.asgi:application -k uvicorn.workers.UvicornWorker