from django.apps import AppConfig


class UserProfileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile_app'

    def ready(self):
        from . signals import create_user_profile
