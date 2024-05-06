from django.apps import AppConfig


class DonateappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donateApp'

    def ready(self):
        import donateApp.signals
