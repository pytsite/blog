"""PytSite Blog Application Models
"""
from pytsite import plugman

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

if plugman.is_installed('article'):
    from plugins import article


    class Article(article.model.Article):
        """Article Content Model
        """
        pass

if plugman.is_installed('page'):
    from plugins import page


    class Page(page.model.Page):
        """Page Content Model
        """
        pass
