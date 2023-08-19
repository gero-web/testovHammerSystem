from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
    
    def ready(self) -> None:
        from .signals import create_profile_signal 
        return super().ready()
