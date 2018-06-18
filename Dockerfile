FROM python:3-alpine

RUN apk update && apk upgrade && apk add --no-cache gcc postgresql-dev git libpq musl-dev linux-headers libffi-dev make

WORKDIR /app

ADD requirements requirements

RUN pip3 install -r requirements/prod.txt --no-cache-dir

ADD . .

RUN mkdir /app/static && \
    mkdir /app/media && \
    mkdir /app/usermedia && \
    mkdir /app/sitemon/settings/local && \
    adduser -D -u 1000 appuser -h /app && chown -R appuser: /app

USER appuser

EXPOSE 8000
