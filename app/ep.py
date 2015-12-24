"""Application Endpoints.
"""
from pytsite import content, tpl, odm, lang, widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def home(args: dict, inp: dict) -> str:
    """Home page.
    """
    exclude_ids = []

    sections = content.get_sections()

    latest = _get_articles(exclude_ids)

    latest_by_section = {}
    for sec in sections:
        latest_by_section[sec.alias] = _get_articles(exclude_ids)

    return tpl.render('content/home', {
        'sections': sections,
        'latest_articles': latest,
        'latest_by_section': latest_by_section,
        'sidebar': _get_sidebar(exclude_ids),
        'language_nav': widget.select.LanguageNav('language-nav'),
    })


def article_index(args: dict, inp: dict) -> str:
    exclude_ids = [e.id for e in args.get('entities')]
    args['sidebar'] = _get_sidebar(exclude_ids)
    args['language_nav'] = widget.select.LanguageNav('language-nav')

    return tpl.render('content/index', args)


def article_view(args: dict, inp: dict) -> str:
    entity = args.get('entity')

    exclude_ids = [entity.id]

    return tpl.render('content/{}'.format(entity.model), {
        'entity': entity,
        'sidebar': _get_sidebar(exclude_ids),
        'related': _get_articles(exclude_ids, 3, entity.section, 'views_count') if entity.model == 'article' else [],
        'language_nav': widget.select.LanguageNav('language-nav'),
    })


def page_view(args: dict, inp: dict) -> str:
    return article_view(args, inp)


def _get_sidebar(exclude_ids: list) -> list:
    r = {
        'popular': _get_articles(exclude_ids, 3, sort_field='views_count'),
        'latest': _get_articles(exclude_ids, 3),
        'tag_cloud': content.widget.TagCloud(
            uid='sidebar-tag-cloud',
            title=lang.t('tags_cloud'),
            css='block',
            term_css='hvr-sweep-to-right',
        ),
    }

    return r


def _get_articles(exclude_ids: list, count: int=5, section: content.model.Section=None, sort_field='publish_time'):
    f = content.find('article').where('_id', 'nin', exclude_ids).sort([(sort_field, odm.I_DESC)])

    if section:
        f.where('section', '=', section)

    r = []
    for article in f.get(count):
        r.append(article)
        exclude_ids.append(article.id)

    return r
