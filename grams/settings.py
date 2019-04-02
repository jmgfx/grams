import os
import django_heroku


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(-fux-wu+4wn+73t2$!rlm7v_%)h1nzh)mcu8aik(ubn6opf2)'

DEBUG = True

ALLOWED_HOSTS = [
    'gramsapp.herokuapp.com',
]

INSTALLED_APPS = [
    # GRAMS apps
    'dashboard',
    'assets.apps.AssetsConfig',
    'transactions.apps.TransactionsConfig',
    'assetBrands.apps.AssetbrandsConfig',
    'assetCategories.apps.AssetcategoriesConfig',
    'vendors.apps.VendorsConfig',
    'branch.apps.BranchConfig',
    'company.apps.CompanyConfig',
    'users',
    # Django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Third party apps
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grams.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'grams/templates/')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'grams.context_processors.Notifications',
                'grams.context_processors.PermissionsAuth',
            ],
        },
    },
]

WSGI_APPLICATION = 'grams.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'jean-grams',
        'PASSWORD': 'garcia',
        'NAME': 'testgrams',
        'TEST': {
            'NAME': 'testgrams',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_PROFILE_MODULE = [
    'users.models.Permissions',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/grams/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'grams/static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_REDIRECT_URL = 'dashboard'

LOGIN_URL = 'login'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

django_heroku.settings(locals())