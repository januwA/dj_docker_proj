#!/bin/sh

sleep 10s

# celery worker
celery multi start 1 -A proj -l ERROR -c4 \
  --pidfile="/var/run/celery/%n.pid" \
  --logfile="/var/log/celery/%n%I.log"

celery multi start 2 -A proj -l ERROR -c4 \
  --pidfile="/var/run/celery/%n.pid" \
  --logfile="/var/log/celery/%n%I.log"
# celery multi restart 1 --pidfile=/var/run/celery/%n.pid

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# daphne -b 127.0.0.1 -p ${DJANGO_PORT} proj.asgi:application
# python manage.py runserver 127.0.0.1:${DJANGO_PORT}
gunicorn -b 127.0.0.1:"${DJANGO_PORT}" proj.asgi:application -k uvicorn.workers.UvicornWorker
