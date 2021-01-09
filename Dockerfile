FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . /api

WORKDIR /api

RUN pip install pipenv
RUN pipenv install
