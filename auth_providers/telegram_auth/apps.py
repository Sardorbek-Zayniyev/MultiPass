from django.apps import AppConfig


class TelegramAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_providers.telegram_auth'
