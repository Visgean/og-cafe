#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: 	Visgean Skeloru 
# email: 	<visgean@gmail.com>
# jabber: 	<visgean@jabber.org>
# github: 	http://github.com/Visgean

import getpass
#import os




PROJECT_NAME = 'trendyou'

location = "/var/www/trendyou/"


templates = location + "templates"
templates_location = templates
MEDIA_ROOT = location + "media/"



	

DATABASES = {
	"default" :  {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'trendyou',                      # Or path to database file if using sqlite3.
        'USER': 'trendyou',                      # Not used with sqlite3.
        'PASSWORD': 'ypyxwlERzcQq',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
}



STATICFILES_DIRS = (
 location + "static/",
 
)

TEMPLATE_DIRS = (
     location + "templates/"
)

DEBUG = True

EMAIL_HOST = 'localhost'
