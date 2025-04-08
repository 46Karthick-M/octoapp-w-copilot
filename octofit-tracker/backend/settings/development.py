# octofit-tracker/octofit-tracker/backend/settings/development.py

import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Development database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Additional development settings can be added here as needed.