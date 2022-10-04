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
git clone https://github.com/SergIvo/dvmn-django-orm-watching-storage
```
2. Use `pip` package manager to install dependencies. Create virtual environment first to avoid conflicts with other versions of the same packages:
```
python -m venv venv
```
Then install dependencies from "requirements.txt" in created virtual environment:
```
pip install -r requirements.txt
```
3. Run "main.py" to start the application. Then you should be able to open it in a web browser by address [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
```
python main.py
```
4. Add data required to establish connection with database, as described in [the lesson](https://dvmn.org/modules/django-orm/lesson/watching-storage/)

