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
router.handle('/section/<term_alias>', 'content@index', 'article_index_by_section', {
    'model': 'article',
    'term_field': 'section',
})

# Index by tag route
router.handle('/tag/<term_alias>', 'content@index', 'article_index_by_tag', {
    'model': 'article',
    'term_field': 'tags',
})

# Index by author route
router.handle('/author/<author>', 'content@index', 'article_index_by_author', {
    'model': 'article',
})

# Lang globals
lang.register_global('app@app_name', lambda language, args: settings.get('app.app_name_' + language, 'The Blog'))

# Tpl globals
tpl.register_global('content_sections', lambda: list(section.get()))
tpl.register_global('content_pages', lambda: list(content.find('page').get()))
