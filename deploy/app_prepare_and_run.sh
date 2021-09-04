#!/bin/bash

# Collect static files
echo "Collect static files"
pipenv run python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
pipenv run python manage.py migrate

# Start server
echo "Starting server"
cd /app
pipenv run uwsgi --http :8000 --wsgi-file /app/test_quiz/wsgi.py
