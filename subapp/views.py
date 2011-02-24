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
  example_obj = {
      'title': 'Title',
      'desc': 'Description',
      'img': 'http://docs.python.org/_static/py.png'
      }
  objects = dict([ (id,obj) for id in ids ] )

  return render_template(request, 'index.html', {
    'objects': ['foo','bar','baz'],
    })

@wsgify(RequestClass=Request)
def read(request):
  return render_template(request, 'show.html', {
    })

@wsgify(RequestClass=Request)
def create(request):
  return render_template(request, 'show.html', {
    })

@wsgify(RequestClass=Request)
def update(request):
  id = request.urlvars.get('id', None)
  return render_template(request, 'show.html', {
    })

@wsgify(RequestClass=Request)
def delete(request):
  id = request.urlvars.get('id', None)
  return render_template(request, 'index.html', {
    })

