# userRegisteration
django project
This is a simple django project, to show you how to start django website development. 
You can follow the following steps to setup a django environment and then download the project and run the command:
python manage.py runserver 
to start the project. 

Steps to set up the django develop envronment:
In mac system

1. Install python
go to this url: https://www.python.org/downloads/mac-osx/
verify: python -V

2. Create a new directory for example 3d

3. Install pip
sudo easy_install pip

4. Go to 3d and install virtualenv
sudo pip install virtualenv

5. Create a Virtual ENV
virtualenv ENV

6. Download Django 
git clone git://github.com/django/django.git

7. Start the virtual environment
source env/bin/activate

8. Install Django in the Virtual ENV
pip install -e django/

9. Here the database I use postgresql so I run the following command:
pip install django psycopg2

10. Build a new project
django-admin.py startproject example

11. Go into the project directory
cd example

12. Go to the settings file change the following database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘postgres’,
        'USER': ‘postgres’,
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ’5432’,
    }
}


13. Migrate some data model to database 
python manage.py makemigrations
python manage.py migrate

14. Create superuser for your admin webpage.
python manage.py createsuperuser

15. And then run server
python manage.py runserver

If meet this error:
library not loaded libssl.1.0.0.dylib django

do the following steps:
$ sudo chown -R $(whoami):admin /usr/local

Once this was done, re-installed psycopg2 and performed the following:

$ sudo ln -s /Library/PostgreSQL/9.3/lib/libssl.1.0.0.dylib /usr/local/lib/
$ sudo ln -s /Library/PostgreSQL/9.3/lib/libcrypto.1.0.0.dylib /usr/local/lib/

















