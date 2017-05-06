"""PytSite Blog Init.
"""
from pytsite import permissions, settings, lang, plugman
from . import model, settings_form

# Permissions
permissions.define_permission('app.settings.manage', 'app@manage_app_settings', 'app')

# Settings
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cube', 'app.settings.manage')

# Lang globals
lang.register_global('app@app_name', lambda language, args: settings.get('app.app_name_' + language, 'The Blog'))

if plugman.is_installed('content'):
    from plugins import content

    if plugman.is_installed('article'):
        # Register 'article' model
        content.register_model('article', model.Article, 'app@articles')

    if plugman.is_installed('page'):
        # Register 'page' model
        content.register_model('page', model.Page, 'app@pages')
