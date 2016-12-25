"""PytSite Blog Init.
"""
from pytsite import content, permissions, settings, router, tpl, lang
from . import model, settings_form


def _app_name(language: str, args: dict):
    return settings.get('app.app_name_' + language, 'The Blog')


# ODM models
content.register_model('article', model.Article, 'app@articles')
content.register_model('page', model.Page, 'app@pages')

# Permissions
permissions.define_permission('app.settings.manage', 'app@manage_app_settings', 'app')

# Settings
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cube', 'app.settings.manage')

# Index by section route
router.add_rule('/section/<string:term_alias>', 'article_index_by_section', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'section',
})

# Index by tag route
router.add_rule('/tag/<string:term_alias>', 'article_index_by_tag', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'tags',
})

# Lang globals
lang.register_global('app_name', _app_name)

# Tpl globals
tpl.register_global('content_sections', lambda: list(content.get_sections()))
tpl.register_global('content_pages', lambda: list(content.find('page').get()))
