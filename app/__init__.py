"""Application Init.
"""
from pytsite import content, permission, settings
from . import model, settings_form

# Register application models
content.register_model('article', model.Article, 'articles')
content.register_model('page', model.Page, 'pages')

# Application settings form
permission.define_permission('app.settings.manage', 'manage_app_settings', 'app')
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cubes', 'app.settings.manage', -999)
