from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pin.apps.profiles"

    def ready(self):
        from pin.apps.profiles import signals
