FROM python:3-alpine

WORKDIR /app

# required by psycopg2-binary in runtime
RUN apk add --no-cache libpq

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock

RUN apk --no-cache add --virtual build-dependencies gcc postgresql-dev musl-dev linux-headers libffi-dev make && \
    pip install pipenv --no-cache-dir && \
    pipenv install --deploy --system && \
    pip uninstall -y pipenv && \
    apk del build-dependencies

ADD . .

RUN mkdir /app/{{ project_name }}/static && \
    mkdir /app/{{ project_name }}/media && \
    mkdir /app/{{ project_name }}/usermedia && \
    adduser -D -u 1000 appuser -h /app && chown -R appuser: /app

USER appuser

ENV DOCKERIZED=1

EXPOSE 8000
