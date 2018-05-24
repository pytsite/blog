"""PytSite Blog
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def app_load():
    from plugins import auth, content
    from . import model

    # Register models
    content.register_model('article', model.Article, 'app@articles')
    content.register_model('page', model.Page, 'app@pages')

    # Ensure that anonymous users can view articles and pages
    for model in content.get_models():
        for r in auth.find_roles():
            if r.name in ('admin', 'dev'):
                continue
            r.permissions = list(r.permissions) + ['odm_auth@view.{}'.format(model)]
            auth.switch_user_to_system()
            r.save()
            auth.restore_user()
