# GRAMS
Giligan's Restaurant Asset Management System


## Set Up

### Dependencies
1. Python 3.7+
2. Django 2.1+

### Instructions
1. Include all apps in the settings.py `INSTALLED_APPS`
2. Append the following at the end:
```
STATIC_URL = '/grams/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'grams/static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
3. Include in `TEMPLATES`:
```
'DIRS': [(os.path.join(BASE_DIR, 'grams/templates/')),],
```
4. Run the following commands
```
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
```
5. Run the server

## Reminders
* Run the collectstatic command whenever you add, modify, or delete a static file.
* Run the makemigrations & migrate commands whenever a change to the database model is made.