# GRAMS
Giligan's Restaurant Asset Management System


## Set Up

### Dependencies
1. Python 3.7+
3. PostgreSQL 11.2+

### Instructions
1. Install required Python packages:
```
pip install -r requirements.txt
```
2. Create a database using PostgreSQL.
3. Acquire & modify the template for `settings.py` as per the configurations below.
4. Run the commands:
```
python manage.py makemigrations
python manage.py migrate
```

### Settings.py Configurations
1. Include all apps in the `INSTALLED_APPS`.
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


## Reminders
* Run the collectstatic command whenever you add, modify, or delete a static file.
* Run the makemigrations & migrate commands whenever a change to the database model is made.


# Information
Capstone Project for Group **Opus Omne**, *A.Y. 2018 - 2019*

University of Santo Tomas, Intitute of Information and Computing Sciences, Department of Information Systems

| Name                      | Position                  |
|---------------------------|---------------------------|
| Neil Kevin T. Baduel      | **Project Manager**           |
| Jeanne Marie O. Garcia    | **Back End Developer**        |
| Marco Sevillano R. Lacson | **Quality Assurance Officer** |
| Charizza Marie C. Mendoza | **Front End Developer**       |