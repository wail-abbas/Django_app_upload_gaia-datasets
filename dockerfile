# base image
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY ./web_app /app

WORKDIR /app

COPY ./entrypoint.sh /

COPY ./.env ./.env

ENTRYPOINT ["sh", "/entrypoint.sh"]