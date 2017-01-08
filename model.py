"""PytSite Blog Models.
"""
from plugins import article, page

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Article(article.model.Article):
    """Article Content Model.
    """
    pass


class Page(page.model.Page):
    """Page Content Model.
    """
    pass
