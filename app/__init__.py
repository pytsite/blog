"""PytSite Blog Init.
"""
from pytsite import lang, content, permissions, settings, router, widget, tpl
from . import model, settings_form

# Resources
lang.register_package('app', 'lang')

# ODM models
content.register_model('article', model.Article, 'app@articles')
content.register_model('page', model.Page, 'app@pages')

# Permissions
permissions.define_permission('app.settings.manage', 'app@manage_app_settings', 'app')

# Settings
settings.define('app', settings_form.Form, __name__ + '@application', 'fa fa-cube', 'app.settings.manage')

# Index by section route
router.add_rule('/section/<string:term_alias>', 'index_by_section', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'section',
})

# Index by tag route
router.add_rule('/tag/<string:term_alias>', 'article_index_by_tag', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'tags',
})

# Prepare language related tpl globals
language_nav = {}
search_input = {}
for l in lang.langs():
    language_nav[l] = str(widget.select.LanguageNav('language-nav', dropdown=True, language=l))
    search_input[l] = str(content.widget.Search('search-article', model='article',
                                                title=lang.t('app@search', language=l), language=l))

# Tpl globals
tpl.register_global('language_nav', language_nav)
tpl.register_global('search_input', search_input)
tpl.register_global('get_content_sections', lambda: list(content.get_sections()))
tpl.register_global('get_content_pages', lambda: list(content.find('page').get()))
