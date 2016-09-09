"""
"""
from datetime import datetime
from pytsite import widget, lang, validation, settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(settings.Form):
    def _setup_widgets(self):
        self.add_widget(widget.input.StringList(
            uid='setting_links',
            weight=10,
            label=lang.t('links'),
            add_btn_label=lang.t('add_link'),
            unique=True,
            rules=validation.rule.Url(),
        ))

        current_year = datetime.now().year
        self.add_widget(widget.input.Integer(
            uid='setting_launch_year',
            weight=20,
            label=lang.t('launch_year'),
            h_size='col-xs-12 col-sm-3 col-md-2 col-lg-1',
            required=True,
            min=1984,
            max=current_year
        ))

        # It is important to call super method AFTER
        super()._setup_widgets()
