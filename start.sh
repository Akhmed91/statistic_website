#!/usr/bin/env bash

# Start Gunicorn processes
echo --: Starting application build
echo --: Creating migration
exec python3 manage.py makemigrations
echo ------: makemigrations complete
echo --: Running migration
exec python3 manage.py migrate
echo ------: migrate complete
echo --: Running collectstatic
exec python3 manage.py collectstatic
echo ------: collectstatic complete
echo Starting Gunicorn.
exec gunicorn helloworld.wsgi:application \
    --bind 0.0.0.0:9010 \
    --workers 3