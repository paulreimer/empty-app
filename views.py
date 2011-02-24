from exc import *

# webapp
import google.appengine.ext.webapp
from google.appengine.ext.webapp import Request, Response
from dec import wsgify

# Project
from middleware import render_template
from settings import settings

@wsgify(RequestClass=Request)
def index(request):
  ids = ['foo','bar','baz']
  obj = {
      'title': 'Title',
      'desc': 'Description',
      'img': 'http://docs.python.org/_static/py.png'
      }
  objects = dict([ (id,obj) for id in ids ] )

  return render_template(request, 'index.html', {
    'objects': objects,
    })

