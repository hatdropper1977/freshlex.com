#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Sobanski'
SITENAME = 'Coins N\' Clouds'
SITEURL = 'https://www.freshlex.com'
#SITEURL = 'http://52.54.218.55:8000'
#HEADER_COVER = 'images/sobanski.jpg'
COLOR_SCHEME_CSS = 'monokai.css'

#PROFILE_IMAGE_URL='images/bsod.jpg'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Amazon Web Services', 'https://aws.amazon.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/hatdropper1977'),
          ('linkedin', 'https://www.linkedin.com/in/johnsobanski/'))

DEFAULT_PAGINATION = 10

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

AUTHORS_BIO = {
  "jsobanski": {
    "name": "John Sobanski",
    "cover": "https://raw.githubusercontent.com/hatdropper1977/freshlex.com/master/content/images/bsod_cropped.jpg",
    "image": "https://raw.githubusercontent.com/hatdropper1977/freshlex.com/master/content/images/sobanski.jpg",
    "website": "https://github.com/hatdropper1977/freshlex.com",
    "location": "Washington, DC",
    "bio": "Electrical Engineer turned Cloud Architect.<p><img src=\'https://d5q4akjun1yjt.cloudfront.net/assets/download.png\' alt=\'Cert\'></p><p>License AWS-ASA-18116 (July 1st 2016 – July 1st 2018)</p>",
    #"linkedin": "https://www.linkedin.com/in/johnsobanski/",
    #"github": "https://github.com/hatdropper1977",
  }
}

#Comments
DISQUS_SITENAME = 'freshlex'

#Github
GITHUB_URL = 'https://github.com/hatdropper1977/freshlex.com'

#MENUITEMS = [('all', '/blog/archives.html')]
MENUITEMS = (
             ('Fork me on GitHub!', 'https://github.com/hatdropper1977/freshlex.com'),
             ('AWS Architecture', '/category/howto'),
             ('Coins', '/category/coins'),
             ('Data Science', '/category/data-science'),
             ('Protocols', '/category/ietf'),
)
