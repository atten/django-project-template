# django-project-template

Start project:

```
django-admin.py startproject --template=https://github.com/atten/django-project-template/zipball/base+celery \
-e py,yml,cfg,sh,conf \
-n Dockerfile -n .gitignore -n .dockerignore \
project_name
```

### Template variants:

* [base](https://github.com/atten/django-project-template/tree/master)
* [base+celery](https://github.com/atten/django-project-template/tree/base+celery) [[compare](https://github.com/atten/django-project-template/compare/master...atten:base+celery?expand=1)]

### Running development server on local machine:

1. Check and edit config if necessary
    ```
    nano {{ project_name }}/config/dev.yml
    ```  
1. Install python packages:
    ```
    pipenv shell && pipenv install
    ```
    In case of bugs, try to downgrade pip version:
    ```
    python3 -m pip install pip==18.0
    ```
1.  Launch docker-compose (without django):
    ```
    docker-compose -f docker-compose.dev.yml up -d
    ```
1.  Run python dev server:
    ```
    ./manage.py runserver 8000
    ```
1.  Run celery with beat:
    ```
    celery worker --app {{ project_name }} -l info -c 1 -B
    ```

    
### Running production server in docker:    
    
1. Check and edit config if necessary
    ```
    nano docker/config/{{ project_name }}-docker.yml
    ```  
1. Run docker build:
    ```
    ./docker/build.sh
    ```
1. Launch docker-compose:
    ```
    docker-compose up -d
    ```
1. Check result:
    ```
    curl -i http://localhost:8000 -H host:{{ project_name }}
    ```
1. Check celery logs (test task will be invoked every 10s):
    ```
    docker-compose logs -f celery
    ```
