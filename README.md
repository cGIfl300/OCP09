# OC_P09 - LITReview

Released on:

- [Github](https://github.com/cgifl300/OCP09/)

# LITReview OC_P09

A Django app for studies. The purpose is to release a MVP based on the django
framework and to release it on heroku cloud.

# Prerequisite

I suppose you ever installed python and git before. If not, consider doing it:

- [ ] You must download and install python, according to your operating system,
  python is freely available at [python.org](https://www.python.org/).
- [ ] You can use [git](https://www.git-scm.com/).

# Setup

## Environment Setup

### Cloning the project

Go into your source directory  
`cd ~/src`  
Then start cloning  
`git clone https://github.com/cgifl300/OCP09`

### Create the venv and install the requirements

Enter the cloned directory  
`cd OCP09`  
`python -m venv venv`  
Activate the venv for linux, bsd or macOS  
`source venv/bin/activate`  
Activate the venv for windows  
`.\venv\Scripts\activate.bat`

### Install requirements

`pip install -r requirements.txt`

### (facultative) Populate a demo database

`python manage.py loaddata db.json`

There are 2 users in this demo database, marc/marc and aurelie/aurelie.

You will also need to get the pictures back.

`tar -xvf media.tar`

### Initialise the dev DB

`python manage.py migrate`

### Create a superuser account

`python manage.py createsuperuser`

### Run the dev server

`python manage.py runserver`

## Notes
- The login creation have no security option, you can register as many account as you need to test the app.
- Files are saved in /media.
- The database is using sqlite on db.sqlite3.

### Internal notes:

- Problem in the db UML Diagram:   
  Hotfixes - Ticket.time_created option auto_add_now didn't exist, replaced by
  auto_now_add.
- Problem with model.py:  
  Hotfixes - body = models.CharField(max_length=8192, blank=True) to body =
  models.TextField(max_length=8192, blank=True) to stick the UML model.
