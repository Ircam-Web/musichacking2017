#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Music and Hacking 2017"
SITEURL = 'http://hacking2017.ircam.fr'
AUTHOR = 'Guillaume Pellerin'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
THEME = '/srv/lib/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'

PATH = '/var/in'
OUTPUT_PATH = '/var/out'
STATIC_PATHS = ['doc', 'images']

BANNER = '/images/photo_hack_1920.jpg'
BANNER_SUBTITLE = 'Instruments, Communities, Values'
BANNER_ALL_PAGES = True

DISPLAY_ARTICLE_INFO_ON_INDEX = False

TIMEZONE = 'Europe/Paris'
#
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5


# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Ircam', 'http://www.ircam.fr'),
          ('Musée du Quai Branly', 'http://www.quaibranly.fr/'),
          ('CNAM', 'http://www.cnam.fr'),
          ('Labex CAP', 'http://www.quaibranly.fr/'),
          ('Music Hack Day', 'http://new.musichackday.org/')
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Ircam/'),
          ('GitHub', 'https://github.com/Ircam-RnD/'),
          )

DISQUS_SITENAME='hacking2017'
GITHUB_USER = 'hacking2017'
TWITTER_CARDS = True
TWITTER_USERNAME = 'musichacking17'
TWITTER_WIDGET_ID = '516222825451888640'

PLUGIN_PATHS = ['/srv/lib/pelican-plugins']
PLUGINS = ['assets', 'i18n_subsites', 'jinja2content', 'sitemap', 'gallery',
        #     'render_math',
        #     'liquid_tags.img', 'liquid_tags.video',
        #    'liquid_tags.youtube', 'liquid_tags.vimeo',
        #    'liquid_tags.include_code',
        #    'liquid_tags.notebook',
           ]

SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = '/var/in/img/gallery/'

PELICANGIT_SOURCE_REPO=PATH
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"

PELICANGIT_DEPLOY_REPO=OUTPUT_PATH
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"
PELICANGIT_DEPLOY_IS_LOCAL_DIR = True

PELICANGIT_USER = "root"
PELICANGIT_WHITELISTED_FILES = [
    "README.md"
]

PELICANGIT_PORT=8888

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}

MARKDOWN = {
    'extensions': ['markdown.extensions.meta',],
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
    },
    'output_format': 'html5',
}

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'Musique et hacking',
        }
    }
