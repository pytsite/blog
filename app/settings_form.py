"""
"""
from datetime import datetime as _datetime
from pytsite import widget as _widget, lang as _lang, validation as _validation, settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(settings.Form):
    def _setup_widgets(self):
        self.add_widget(_widget.input.StringList(
            uid='setting_links',
            weight=10,
            label=_lang.t('links'),
            add_btn_label=_lang.t('add_link'),
            unique=True,
            rules=_validation.rule.Url(),
        ))

        current_year = _datetime.now().year
        self.add_widget(_widget.input.Integer(
            uid='setting_launch_year',
            weight=20,
            label=_lang.t('launch_year'),
            h_size='col-xs-12 col-sm-3 col-md-2 col-lg-1',
            required=True,
            min=1984,
            max=current_year
        ))

        # It is important to call super method AFTER
        super()._setup_widgets()
