# django-project-template

Start project:

```
django-admin.py startproject --template=https://github.com/atten/django-project-template/zipball/master \
-e py,yml,cfg,sh,conf \
-n Dockerfile -n .gitignore -n .dockerignore \
project_name
```

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
1.  Run python dev server:
    ```
    ./manage.py runserver 8000
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
 
  