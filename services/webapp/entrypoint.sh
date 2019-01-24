#!/bin/sh

echo "Waiting for postges..."

while ! nc -z webapi-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0

