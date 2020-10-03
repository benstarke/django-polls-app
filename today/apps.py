from django.apps import AppConfig


class TodayConfig(AppConfig):
    name = 'today'

    def ready(self):
        import today.signals



