# Feedback App (Python + Flask + PostgreSQL + Heroku)

Follow this steps and check the code to build and deploy a simple feedback app that an be used as a template for future projects.

## Project setup

1. Install virtual environment manager: `pip install pipenv`

2. Create environment: `pipenv shell` (Close env: `exit`)

3. Install Flask within VE: `pipenv install flask` (It will create a lock file for dependencies)

4. Install psycopg2 (PostgreSQL adapter): `pipenv install psycopg2` (Install psycopg2-binary if some issue appears)

5. Install sqlalchemy (SQL Toolkit and ORM): `pipenv install flask-sqlalchemy`

6. Instal gunicorn (Unix server): `pipenv install gunicorn`

7. Make sure you have correct interpreter: _Ctrl/Cmnd + Shift + p_ -> "Python: Select interpreter" -> _python...(my_app)_

## PostgreSQL setup

1. Download and install postgreSQL from web page to be able to start pgAdmin4 locally

2. Create database using left panel

3. Create table based in model using REPL. Type `python` and run the following (assuming code is ready). After run app again, the table should be visible in pgAdmin4 Schemes panel:
    - `from app import db`
    - `db.create_all()`
    - `exit()`

## Mailtrap setup

1. Create an account to get your credentials and prepare send email service

## Deploy

1. Create Heroku account and download-install Heroku CLI. Also, Git version control is needed
