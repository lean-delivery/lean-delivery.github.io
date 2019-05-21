#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lean Delivery'
SITENAME = u'Lean delivery'
SITEURL = 'https://lean-delivery.com'
THEME = "./epam-theme/"
THEME_STATIC_DIR = 'static'
LOAD_CONTENT_CACHE = False
PATH = 'content'

TIMEZONE = 'Europe/Minsk'

MENUITEMS = (
        ('Catgegories', SITEURL + '/catgegories.html'),
        ('Tags', SITEURL + '/tags.html')
    )

DEFAULT_LANG = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Epam', 'https://epam.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DISQUS_SITENAME = "lean-delivery"

DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#STATIC_PATHS = ['{{ THEME_STATIC_DIR }}']

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors'
]

# Sitemap
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

### Theme specific settings

HEADER_COVER = THEME_STATIC_DIR + '/images/welcome.jpg'
COLOR_SCHEME_CSS = 'github.css'

#Custom Header

HEADER_COVERS_BY_TAG = {
    'cupcake': THEME_STATIC_DIR + '/images/rainbow_cupcake_cover.jpg',
    'general': THEME_STATIC_DIR + '/images/welcome.jpg'
}

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
