from os import environ, path
environ['PYTSITE_APP_ROOT'] = path.dirname(__file__)

from pytsite import wsgi
application = wsgi.application
