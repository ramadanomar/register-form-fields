from django.apps import AppConfig


class YourCustomPluginConfig(AppConfig):
    name = 'registerformfields'

    def ready(self):
        import registerformfields.signals  # noqa
