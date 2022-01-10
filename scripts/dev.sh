#!/bin/bash

# wait db
sleep 10s

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:"${DJANGO_PORT}"