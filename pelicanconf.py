#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Sobanski'
SITENAME = 'FreshLex, LLC'
SITEURL = 'https://freshlex.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Let\'s Encrypt', 'https://letsencrypt.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Amazon Web Services', 'https://aws.amazon.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/hatdropper1977'), )

DEFAULT_PAGINATION = 10

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

AUTHORS_BIO = {
  "jsobanski": {
    "name": "John Sobanski",
    "cover": "http://1.gravatar.com/avatar/d9333b82b60f9f3714a39f9aad419633?s=75&d=mm&r=g",
    "image": "http://1.gravatar.com/avatar/d9333b82b60f9f3714a39f9aad419633?s=75&d=mm&r=g",
    "website": "http://blog.arulraj.net",
    "location": "Washington, DC",
    "bio": "Electrical Engineer turned Cloud Architect.<p><img src=\'https://d5q4akjun1yjt.cloudfront.net/assets/download.png\' alt=\'Cert\'></p><p>Amazon Web Services Certified Solution Architect Associate</p><p>License AWS-ASA-18116 (July 1st 2016 – July 1st 2018)</p>"
  }
}

#Comments
DISQUS_SITENAME = 'www.freshlex.com'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
