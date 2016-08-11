from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = '-&9m(&%3zn(6o1ir#a)zyn=)5bt)95=h1+$*%cqlbm_7flv3!s'