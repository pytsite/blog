"""PytSite Application Simple Theme.
"""
from pytsite import content, events, widget, lang, assetman, browser, router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

router.add_rule('/', '$theme.ep.home')

browser.include('bootstrap', True)
assetman.add('css/common.css', True)
assetman.add('js/common.js', True)

# Inject common arguments on every template
events.listen('pytsite.tpl.render', lambda args: args.update({
    'language_nav': widget.select.LanguageNav('language-nav'),
}))
