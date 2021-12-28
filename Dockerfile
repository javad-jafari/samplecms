# pull the official base image
FROM python:3.6-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies


# install dependencies
RUN pip install --upgrade pip 
COPY ./requierment.txt /usr/src/app
RUN pip install -r requierment.txt

# copy project
COPY . /usr/src/app