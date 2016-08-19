"""PytSite Application Default Theme.
"""
from pytsite import content, widget, lang, assetman, browser, router, tpl, settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Home route
router.add_rule('/', '$theme@home')

# Index by section route
router.add_rule('/section/<string:term_alias>', 'app.article.index@section', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'section',
})

# Index by tag route
router.add_rule('/tag/<string:term_alias>', 'app.article.index@tag', 'pytsite.content@index', {
    'model': 'article',
    'term_field': 'tags',
})

# Prepare language related tpl globals
language_nav = {}
search_input = {}
for l in lang.langs():
    language_nav[l] = str(widget.select.LanguageNav('language-nav', dropdown=True, language=l))
    search_input[l] = str(content.widget.Search('search-article', model='article', title=lang.t('search', language=l),
                                                language=l))
# Registering tpl globals
tpl.register_global('language_nav', language_nav)
tpl.register_global('search_input', search_input)
tpl.register_global('get_content_sections', lambda: list(content.get_sections()))
tpl.register_global('get_content_pages', lambda: list(content.find('page').get()))

# Permanent assets
browser.include('bootstrap', True)
assetman.add('css/common.css', True)
assetman.add('js/common.js', True)
