from django.urls import path
from . import views

urlpatterns = [
    path('generate-email-otp', views.generate_email_otp, name='generate_email_otp'),
    path('verify-email-otp', views.verify_email_otp, name='verify_email_otp'),
]
