"""PytSite Blog Init.
"""
from pytsite import permissions, settings, router, tpl, lang
from plugins import content, section
from . import model, settings_form


# ODM models
content.register_model('article', model.Article, 'app@articles')
content.register_model('page', model.Page, 'app@pages')

# Permissions
permissions.define_permission('app.settings.manage', 'app@manage_app_settings', 'app')

# Settings
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cube', 'app.settings.manage')

# Index by section route
router.add_rule('/section/<string:term_alias>', 'article_index_by_section', 'content@index', {
    'model': 'article',
    'term_field': 'section',
})

# Index by tag route
router.add_rule('/tag/<string:term_alias>', 'article_index_by_tag', 'content@index', {
    'model': 'article',
    'term_field': 'tags',
})

# Lang globals
lang.register_global('app@app_name', lambda language, args: settings.get('app.app_name_' + language, 'The Blog'))

# Tpl globals
tpl.register_global('content_sections', lambda: list(section.get()))
tpl.register_global('content_pages', lambda: list(content.find('page').get()))
