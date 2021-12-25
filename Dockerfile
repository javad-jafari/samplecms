# pull the official base image
FROM python:3.6-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD=admin

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip 
COPY ./requierment.txt /usr/src/app
RUN pip install -r requierment.txt

# copy project
COPY . /usr/src/app

RUN  python manage.py makemigrations --noinput 
RUN  python manage.py migrate --noinput 
RUN  python manage.py createsuperuser  --user admin --email admin@info.com --noinput
 
