#!/usr/bin/env bash

psql postgres -f $VIRTUAL_ENV/dev/cleandb.sql

$VIRTUAL_ENV/manage.py migrate

export DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:=admin}
export DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:=admin@example.com}
export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:=secret}

$VIRTUAL_ENV/manage.py createsuperuser --noinput

echo Superuser username: $DJANGO_SUPERUSER_USERNAME
echo Superuser password: $DJANGO_SUPERUSER_PASSWORD