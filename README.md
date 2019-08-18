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

2. Run `heroku login` to connect to your account

3. Create Heroku app with `heroku create [app name]`

4. Create a Heroku database using Heroku addons for PostgreSQL: `heroku addons:create heroku-postgresql:hobby-dev --app [app name]`

5. Get new database URL (then, set your SQLALCHEMY_DATABASE_URI for production): `heroku config --app [app name]`

6. Create requirements file with dependencies: `pip freeze > requirements.txt`

7. Create Procfile, so Heroku, as a Paas, will know how to run the app: `touch Procfile` (Unix). Here, we set gunicorn as our server

8. Create runtime file to specify Python version

9. Push everithing to remote git repository

10. 
