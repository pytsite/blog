"""Application Init.
"""
from pytsite import content
from . import model

# Register application models
content.register_model('article', model.Article, 'articles')
content.register_model('page', model.Page, 'pages')
