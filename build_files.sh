#!/bin/bash
set -e
pip install -r requirements.txt --break-system-packages
DATABASE_URL="" python manage.py collectstatic --noinput
