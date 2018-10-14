#!/usr/bin/env bash

docker build -t {{ project_name }}:latest \
             -t {{ project_name }}:0.0.1 \
             .