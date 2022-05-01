from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ayvuapp.users'

    def ready(self):
        try:
            import ayvuapp.users.signals  # noqa F401
        except ImportError:
            pass
