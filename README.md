# spotter-bookverse
Library project owned by me crafted and fine tuned for Spotter.ai


[![CodeQL](https://github.com/sifykarippery/spotter-bookverse/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/sifykarippery/spotter-bookverse/actions/workflows/codeql.yml)

[![black-flake8-isort-hooks](https://github.com/sifykarippery/spotter-bookverse/actions/workflows/black-flake8-isort-hooks.yml/badge.svg)](https://github.com/sifykarippery/spotter-bookverse/actions/workflows/black-flake8-isort-hooks.yml)

### Setting Up Project

1. Install Setup pyenv - with 3.12
2. Install Pipenv

```
    pyenv local 3.12
    pipenv install     # have 3.12 python used for project
    pipenv shell       # activate python env using pipenv

```
3. Install Django and Django Rest Framework

```
    pipenv install django
    pipenv install djangorestframework

```

4. Install & Setup Project

```
    django-admin startproject bookverse
    django-admin startapp api

```


python manage.py runserver

user = User.objects.create_user('akshay', 'email@example.com', 'password')
user=User.objects.create_user('admin', password='admin')

Api User: api
ApiPassword: apiUser@123


{
    "username": "apiapi",
    "password": "Apiapi@123",
    "email": "apiJwt@example.com"
}


5. Test your code always with
black
isort
flake8
