"""PytSite Blog Settings Form
"""
from pytsite import widget, lang, validation, settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(settings.Form):
    """PytSite Blog Settings Form.
    """
    def _on_setup_widgets(self):
        """Hook.
        """
        # Application names
        w = 10
        for l in lang.langs(include_neutral=False):
            self.add_widget(widget.input.Text(
                uid='setting_app_name_' + l,
                weight=w,
                label=lang.t('app@application_name', {'lang': lang.lang_title(l)}),
                default=lang.t('app@app_name'),
            ))

            w += 1

        # Links
        self.add_widget(widget.input.StringList(
            uid='setting_links',
            weight=20,
            label=lang.t('app@links'),
            add_btn_label=lang.t('app@add_link'),
            unique=True,
            rules=validation.rule.Url(),
        ))

        # It is important to call super method AFTER
        super()._on_setup_widgets()
