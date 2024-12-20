from django.apps import AppConfig


class EmailPasswordAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_providers.email_password_auth'
