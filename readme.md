# Install

```bash
# create project directory
django-admin startproject django_cms

# go to project
cd django_cms

# create virtualenv directory
virtualenv -p /usr/bin/python2.7 venv

# active virtualenv
source venv/bin/activate

# create app directory
django-admin startapp cms

# install package for virtualenv
pip install django

# Run migrate to create basic tables.
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Running server for testing
python manage.py runserver 0.0.0.0:9160
```

## Start working

* Go to `http://127.0.0.1:9160/admin` and login.

* For TinyMCE :

checkout the link 
[Package File Browser](https://django-filebrowser.readthedocs.io/en/latest/quickstart.html)
[Package TinyMCE](http://django-tinymce.readthedocs.io/en/latest/installation.html)

```bash
pip install django-tinymce
pip install django-filebrowser
pip install Image
```

Setup `STATIC_ROOT` by adding to `settings.py`

```bash
STATIC_ROOT = "/var/www/html/django_cms/static/"
python manage.py collectstatic
```
* Create models and run:

```bash
python manage.py makemigrations
Migrations for 'cms':
  cms/migrations/0001_initial.py:
    - Create model Category
    - Create model Post
python manage.py migrate
```
