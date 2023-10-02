# Backend Assignment 

## Setup project

The first thing to do is to clone the repository:

```sh
git clone https://github.com/anmol8275/Backend-Assignment.git
```

## Create virtualenv
```sh
pip install virtualenv
python<version> -m venv <virtual-environment-name>
```
Note: Please install python version >=3.8 

## Activate virtual environment
```sh
source venv/bin/activate
```

## Install dependencies

```sh
pip install -r requirements.txt
```

## Create .env file in the same directory where `manage.py` is
Add below variables in .env file
```sh
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_NAME=backend_assignment
POSTGRES_USER=backend_assignment
POSTGRES_PASSWORD=backend_assignment@1234
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
ACCESS_TOKEN_LIFETIME_MINUTES=10
REFRESH_TOKEN_LIFETIME_DAYS=30
SITE_NAME=Backend Assignment
BACKEND_DOMAIN=localhost:8000
DRF_SPECTACULAR=True
```
Note: Please set database values as per your database name

## Perform database migrations

To run the migration, `cd` into the directory where `manage.py` is:
```sh
python manage.py migrate
```

After migrations are applied, create a Development Django user:

## Create superuser

To create superuser, `cd` into the directory where `manage.py` is:
```sh
python manage.py createsuperuser
```

## Run project 
Change `cd` into the directory where `manage.py` is:
```sh
python manage.py runserver
```
Browse the REST API doc at:
```sh
http://localhost:8000/api/redoc/
```
