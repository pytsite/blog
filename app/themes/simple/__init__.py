"""PytSite Application Simple Theme.
"""
from pytsite import events, widget, assetman, browser, router, content, lang

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

router.add_rule('/', '$theme@home')

browser.include('bootstrap', True)
assetman.add('css/common.css', True)
assetman.add('js/common.js', True)

# Inject common arguments on every template
events.listen('pytsite.tpl.render', lambda tpl, args: args.update({
    'sections': list(content.get_sections()),
    'pages': content.find('page').get(),
    'language_nav': widget.select.LanguageNav('language-nav'),
    'search_widget': content.widget.Search('search-article', model='article', title=lang.t('search')),
}))
