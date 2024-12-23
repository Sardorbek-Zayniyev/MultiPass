from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_number_login, name='phone_number_login'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]
