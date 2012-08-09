# Django settings for Lisculea project.

import os
import platform

DEBUG = True
#TEMPLATE_DEBUG = DEBUG
TEMPLATE_DEBUG = True

ADMINS = (
     ('a3soft', 'a3soft@gmail.com'),
)

MANAGERS = ADMINS


# set path to Lisculea, both on windows and linux 
home = os.path.expanduser("~")

if platform.system() == "Windows":
    pathToLisculea = os.sep.join(["C:", "VinasData", "Lisculea", "Lisculea", ""])
    
if platform.system() == "Linux":
    pathToLisculea = os.sep.join([home, "scripty", "Lisculea", "Lisculea", ""])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': pathToLisculea + "sqlite.db",    # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cz-cs'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = pathToLisculea + "static"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's@$k1i-3^uk0ui4@w&yzyfdv8v0!q)l-uo*jrhub62c=p^m8tl'


SERIALIZATION_MODULES = {
#    'yml': "django.core.serializers.pyyaml"
} 



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.auth',
)


TEMPLATE_DIRS = (
    pathToLisculea  + "Templates"
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = (
    '127.0.0.1',
)


ROOT_URLCONF = 'Lisculea.urls'
LOGIN_URL = "/general/login/"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    "django.contrib.markup",
    "django.contrib.humanize",
#    "registration",
    "debug_toolbar",
    "Lisculea.General",
    "Lisculea.Grades",
    "Lisculea.FileShare",
    "Lisculea.Cafe",
    "Lisculea.Luncher",
)

ACCOUNT_ACTIVATION_DAYS = 3

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


DEBUG_TOOLBAR_CONFIG = {
                        "INTERCEPT_REDIRECTS" : False}
