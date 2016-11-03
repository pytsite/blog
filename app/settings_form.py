"""Application Settings Form.
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

        # It is important to call super method AFTER
        super()._setup_widgets()
