#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Julian Wishahi'
SITENAME = u'PauschaleAussagen'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

THEME = "theme/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly'

CC_LICENSE = 'CC-BY-SA'
#CC_ATTR_MARKUP = True

# Article info
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('github', 'https://github.com/pauschaleaussagen'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/PauschalAussage'),
          ('github' , 'http://github.com/pauschaleaussagen'),)

DEFAULT_PAGINATION = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME'     : {'path' : 'CNAME'},
		       'extra/README'    : {'path' : 'README'},
		       'extra/LICENSE'   : {'path' : 'LICENSE'},
		       'extra/.htaccess' : {'path' : '.htaccess'},
		      }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
