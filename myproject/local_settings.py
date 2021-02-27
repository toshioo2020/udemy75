import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'v!hf$jrvqn)57xtqe46x90z_salq^ckl1!pviixkxxzxo-@yzt'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}