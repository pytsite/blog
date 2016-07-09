"""Application Endpoints.
"""
from pytsite import content, tpl, addthis, reg, comments

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def home(args: dict, inp: dict) -> str:
    """Home page.
    """
    args['articles'] = list(content.find('article').get())

    return tpl.render('content/home', args)


def content_article_view(args: dict, inp: dict) -> str:
    """Article view.
    """
    e = args['entity']

    comments_widget = ''
    if 'pytsite.disqus' in reg.get('app.autoload'):
        comments_widget = comments.get_widget('disqus')
    elif 'pytsite.fb' in reg.get('app.autoload'):
        comments_widget = comments.get_widget('fb')

    args.update({
        'entity_tags': content.widget.EntityTagCloud('entity-tag-cloud', entity=args['entity']),
        'share_widget': addthis.widget.AddThis('add-this-share') if reg.get('addthis.pub_id') else '',
        'comments_widget': comments_widget,
    })

    return tpl.render('content/{}'.format(e.model), args)


def content_page_view(args: dict, inp: dict) -> str:
    """Page view.
    """
    return content_article_view(args, inp)
