# Backend Assignment 

## Setup project

The first thing to do is to clone the repository:

```sh
$ git clone git@bitbucket.org:trootechteam/quixom-backend.git
```
## Install Pyenv on Linux
Setup Venv:

1)Install pyenv:
```sh
$udo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git```

```sh
curl https://pyenv.run | bash
```
```sh
$ git clone https://github.com/pyenv/pyenv-virtualenv.git
$(pyenv root)/plugins/pyenv-virtualenv
```
2)Then need to add this to .bashrc (in home directory)
```sh

 export PATH="$HOME/.pyenv/bin:$PATH"
 eval "$(pyenv init -)"
 eval "$(pyenv virtualenv-init -)"
```
exec $SHELL

3) Install Python

```sh
pyenv install <version>
pyenv virtualenv <version> <virtual_env_name>
```
4) Activate Venv

```sh
source .pyenv/versions/<virtual_env_name>/bin/activate 
```
OR
```sh
pyenv activate <virtual_env_name>
```
## Install dependencies

```sh
cd quixom-backend/quixom-backend/quixom-backend
(venv)$ pip install -r ../requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies then apply migrations:

## Perform database migrations

To run the migration, `cd` into the directory where `manage.py` is:
```sh
(venv)$ python manage.py migrate
```

After apply migrations Create a Development Django user:

## Create superuser

To create superuser, `cd` into the directory where `manage.py` is:
```sh
(venv)$ python manage.py createsuperuser
```

## Run project 
Change `cd` into the directory where `manage.py` is:
```sh
(venv)$ python manage.py runserver
```
Browse the REST API at:
## Getting Home page api response
[http://localhost:8000/api/v1/cms/pages/home/](http://localhost:8000/api/v1/cms/pages/home/).
