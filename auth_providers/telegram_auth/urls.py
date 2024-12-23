from django.urls import path
from . import views
urlpatterns = [
    path('callback/', views.telegram_callback, name='telegram_callback'),
]
