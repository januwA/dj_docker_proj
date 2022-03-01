#!/bin/sh

sleep 10s

# celery worker
celery multi start 1 -A proj -l INFO -c4 \
  --pidfile="/var/run/celery/%n.pid" \
  --logfile="/var/log/celery/%n%I.log"
# celery multi restart 1 --pidfile=/var/run/celery/%n.pid
# celery multi stopwait 1 --pidfile=/var/run/celery/%n.pid
# celery multi -h

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:"${DJANGO_PORT}"
