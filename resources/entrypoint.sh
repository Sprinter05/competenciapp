#! /bin/bash

# Create migrations for the models
python manage.py makemigrations core

# Repeat until migration is OK
until python manage.py migrate
do
    echo "Migration failed! Retrying..."
    sleep 1
done

# Run the server
python manage.py runserver 0.0.0.0:8000