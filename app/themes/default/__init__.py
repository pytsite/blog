"""PytSite Blog Default Theme Package.
"""
from pytsite import content, events, widget, lang, assetman, browser, router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Routes
router.add_rule('/', '$theme.ep.home')
router.add_rule('/section/<string:term_alias>', 'app.article.index.section', 'pytsite.content.ep.index', {
    'model': 'article',
    'term_field': 'section',
})
router.add_rule('/tag/<string:term_alias>', 'app.article.index.tag', 'pytsite.content.ep.index', {
    'model': 'article',
    'term_field': 'tags',
})

# Inject common arguments on every template
events.listen('pytsite.tpl.render', lambda args: args.update({
    'sections': list(content.get_sections()),
    'pages': content.find('page').get(),
    'language_nav': widget.select.LanguageNav('language-nav'),
    'search_widget': content.widget.Search('search-article', model='article', title=lang.t('search')),
}))

browser.include('bootstrap', True)
assetman.add('css/common.css', True)
assetman.add('js/common.js', True)
