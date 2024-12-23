from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    otp_enabled = models.BooleanField(default=False)
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    auth_date = models.DateTimeField(null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    telegram_username = models.CharField(
        max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
