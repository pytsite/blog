"""Application Init.
"""
from pytsite import content, events, widget, lang
from . import model

# Register application models
content.register_model('article', model.Article, 'articles')
content.register_model('page', model.Page, 'pages')

# Inject common arguments on every template render event
events.listen('pytsite.tpl.render', lambda args: args.update({
    'sections': list(content.get_sections()),
    'pages': content.find('page').get(),
    'language_nav': widget.select.LanguageNav('language-nav'),
    'search_widget': content.widget.Search('search-article', model='article', title=lang.t('search')),
}))
