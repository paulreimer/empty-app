# Templates
from jinja2 import Environment, FileSystemLoader
import os
import inspect

basename = lambda path: os.path.dirname(os.path.abspath(path))

def render_template(request, template, context):
  importing_file = inspect.stack()[1][1]

  template_dirs = [
      os.path.join(basename(__file__),'templates'),
      os.path.join(basename(importing_file),'templates'),
      ]
  templates = Environment(loader=FileSystemLoader(template_dirs))

  template = templates.get_template('index.html')
  body = template.render(context)

  if not body:
    body = request.response
    resp.status_int = 404
    #resp.status = "404 Template '"+template+"' not found"

  return body

