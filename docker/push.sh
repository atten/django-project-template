#!/usr/bin/env bash

docker push {{ project_name }}:latest
docker push {{ project_name }}:0.0.1