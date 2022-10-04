# Watching Storage Dashboard

## About

This is a small Django application made for educational purposes as part of an online course at [dvmn.org](https://dvmn.org/). An application designed to meet requirements listed in [this lesson](https://dvmn.org/modules/django-orm/lesson/watching-storage/) from the Django ORM module of mentioned course.

As a simple control point dashboard, an application performs the following tasks:

* Querying data about storage visitors by presetted conditions from database using the Django ORM;
* Calculates the duration of the visitor's presence in the storage;
* Format this information to make it more human-readable and presents it via web interface.

## Running the application

1. Download application files from GitHub using `git clone` command:
```
git clone https://github.com/SergIvo/django-orm-local
```
2. Before installing necessary packages, create virtual environment to avoid conflicts with other versions of the same packages:
```
python -m venv venv
```
Then install dependencies from "requirements.txt" in created virtual environment. Use `pip` package manager to install packages listed in `requirements.txt`:
```
pip install -r requirements.txt
```
3. Before running the application, you should set some environment variables, like database connection setting or django secret key:
```
export DB_HOST='Database host name'
export DB_PORT='Port on which database accepts connection'
export DB_NAME='Name of the database'
export DB_USER='Username for database user'
export DB_PASSWORD='Password for database user'
export DJANGO_SECRET_KEY='Randomly generated secret key'
export DEBUG='Set "true" if you want to run application in a debug mode'
```
If you are following the same course, you can get database settings from [the lesson](https://dvmn.org/modules/django-orm/lesson/watching-storage/)

If you don't want to set environment variables manually, you can create [.env](https://pypi.org/project/python-dotenv/#getting-started) file and store all variables in it.
4. Run "manage.py runserver" to start the application. Then you should be able to open it in a web browser by address [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
```
python manage.py runserver
```
