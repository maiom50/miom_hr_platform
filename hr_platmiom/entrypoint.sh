#!/bin/bash
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn hr_platmiom.wsgi:application -b 0.0.0.0:8000 --workers 3 --threads 3