"""PytSite Blog
"""
from pytsite import plugman

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

if plugman.is_installed('content'):
    from plugins import auth, content
    from . import model

    if plugman.is_installed('article'):
        # Register 'article' model
        content.register_model('article', model.Article, 'app@articles')

    if plugman.is_installed('page'):
        # Register 'page' model
        content.register_model('page', model.Page, 'app@pages')

    # Allow all to view content
    auth.switch_user_to_system()
    for model in content.get_models():
        for r in auth.get_roles():
            if r.name == 'admin':
                continue

            r.permissions = list(r.permissions) + [
                'pytsite.odm_auth.view.{}'.format(model),
            ]

            r.save()
    auth.restore_user()
