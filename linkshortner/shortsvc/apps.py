from django.apps import AppConfig


class ShortsvcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortsvc'

    def ready(self):
        import shortsvc.signals