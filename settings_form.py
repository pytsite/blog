"""PytSite Blog Settings Form.
"""
from pytsite import widget, lang, validation, settings, router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(settings.Form):
    """PytSite Blog Settings Form.
    """

    def _setup_widgets(self):
        """Hook.
        """
        w = 10
        for l in lang.langs():
            self.add_widget(widget.input.Text(
                uid='setting_app_name_' + l,
                weight=w,
                label=lang.t('app@application_name', {'lang': lang.lang_title(l)}),
                default=lang.t('app_name'),
            ))

            w += 10

        self.add_widget(widget.input.StringList(
            uid='setting_links',
            weight=w,
            label=lang.t('app@links'),
            add_btn_label=lang.t('app@add_link'),
            unique=True,
            rules=validation.rule.Url(),
        ))

        # It is important to call super method AFTER
        super()._setup_widgets()
