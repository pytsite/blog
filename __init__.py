"""PytSite Blog
"""
from pytsite import plugman

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

if plugman.is_installed('content'):
    from plugins import content
    from . import model

    if plugman.is_installed('article'):
        # Register 'article' model
        content.register_model('article', model.Article, 'app@articles')

    if plugman.is_installed('page'):
        # Register 'page' model
        content.register_model('page', model.Page, 'app@pages')
