"""Application Init.
"""
from pytsite import content, permissions, settings
from . import model, settings_form

# Register application models
content.register_model('article', model.Article, 'articles')
content.register_model('page', model.Page, 'pages')

# Register application settings form
permissions.define_permission('app.settings.manage', 'manage_app_settings', 'app')
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cube', 'app.settings.manage', -999)
