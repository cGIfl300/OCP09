# HEROKU
How to put the app in production on Heroku.
## Create your account
You first need a Heroku account. Create one.
## settings.py
You have to modify `settings.py`.
### DEBUG
You can use a global ENV variable to switch from dev to prod, to automatically
turn DEBUG to False when in production mode and use conditional code.
```python3
if os.environ.get('ENV')=='PRODUCTION':
    DEBUG=False
else:
    DEBUG=True
```
### SECRET_KEY
Generate a new `SECRET_KEY`.  
Launch a python console and enter the code belong.
```python3
import random, string
"".join([random.choice(string.printable) for _ in range(24)])
```

[comment]: <> (Replace the `SECRET_KEY` in your `settings.py`.)

### ALLOWED_HOSTS
Heroku host your app (by default <i>something.herokuapp.com</i>).
Add the domain to the `ALLOWED_HOSTS`. You can add many.
```python3
ALLOWED_HOSTS=['something.herokuapp.com']
```
### Static files
Collect every static files into a file we name `staticfiles` at the root of the
project.  
#### Copy static files
You need to copy every static files into a folder named `static` at the root of
your project (not the app).
#### Create the staticfiles
Add these lines to `settings.py` for django to make the staticfiles. The command
to make this staticfiles is `collectstatic` you don't need to run it, Heroku
will.  
We also add the whitenoise storage when in production mode for later use.  
```python3
if os.environ.get('ENV') == 'PRODUCTION':
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )
    
    STATICFILES_STORAGE =
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
#### Serving files over whitenoise
To serve static files, we need an extra app, named whitenoise. This is not a
part of django project.
##### Install whitenoise
`python -m pip install whitenoise`
##### Add whitenoise to middleware
On `settings.py` add whitenoise to middleware apps.
```python3
MIDDLEWARE = [
    # ... You middlewares above ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```
### Procfile
Add a file, named `Procfile` at the root of your project
```Procfile
web: gnuicorn OCP09.wsgi
```
### Requirements
Generate it using pip.
```shell
pip freeze > requirements.txt
```
## Heroku
You need to install heroku-cli. We will interact with heroku using it and git.
### Adding the missing files to git
`git add .`
`git commit -m 'Production'`
### Force the tracking of our new static folder
By adding a .gitignore file in.
`touch OCP09/static/.gitignore`
#### Edit our new .gitignore
```gitignore
!.gitignore
```
#### Force git tracking
```shell
git add OCP09/static/.gitignore
git commit -m "track static file"
```
### Create the heroku app
```shell
heroku create ocp09
```
### Save environment variables
Your SECRET_KEY
```shell
heroku config:set SECRET_KEY="...your secret key here..."
```
Set ENV
```shell
heroku config:set ENV="PRODUCTION"
```
Show our different environment variables
```shell
heroku config
```
### Push our files to heroku
```shell
git push heroku master
```
### Migrate our database
```shell
heroku run python manage.py migrate
```
### Create a superuser
```shell
heroku run python manage.py createsuperuser
```
### Populate database
You can use a json file, you stored on the project to load data to the database.
```shell
heroku run python manage.py loaddata store/dumps/store.json
```
## Enjoy
You can now enjoy your app, here
[ocp09.herokuapp.com](https://ocp09.herokuapp.com/) or wherever will be hosted
your app.