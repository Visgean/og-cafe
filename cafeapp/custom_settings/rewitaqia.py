#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getpass

sys.path.append("/home/visgean/scripty/pymodules/") # django modules like django_filters

USER_HOME_FOLDER = 'visgean'
PROJECT_NAME = 'ogcafe'
location = "/home/visgean/scripty/cafe/"

if getpass.getuser() == "visgean":
	DATABASES = {
		"default" :  {
	        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': location + "sqlite.db", # Or path to database file if using sqlite3.
	        'USER': '', # Not used with sqlite3.
	        'PASSWORD': '', # Not used with sqlite3.
	        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '', # Set to empty string for default. Not used with sqlite3.
	        

	        }
	}
	
else: 
	DATABASES = {
		"default" :  {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'django_' + PROJECT_NAME, # Or path to database file if using sqlite3.
	        'USER': 'django', # Not used with sqlite3.
	        'PASSWORD': 'WpmMMCo7GiWK', # Not used with sqlite3.
	        'HOST': '127.0.0.1', # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '', # Set to empty string for default. Not used with sqlite3.
	        }
	}


templates = location + "/templates"
templates_location = templates
MEDIA_ROOT = location + "media/"

STATICFILES_DIRS = (location + "static/",)

TEMPLATE_DIRS = (location + "templates/",)

DEBUG = True

EMAIL_HOST = 'localhost'



