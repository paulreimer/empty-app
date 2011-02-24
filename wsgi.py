#!/usr/bin/env python
import sys, os

## App Engine
from google.appengine.ext.webapp import util

## Features
# RESTful routing
import selector

from settings import settings
if settings['debug']:
  import logging
  logging.getLogger().setLevel(logging.DEBUG)

rules = [
  ]

def main():
  urls = os.path.join(os.path.dirname(__file__), 'urls.py')
  s    = selector.Selector(mapfile=urls)
  app  = selector.MiddlewareComposer(s, rules)
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

