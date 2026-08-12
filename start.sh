#!/bin/bash
set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn fstp.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
