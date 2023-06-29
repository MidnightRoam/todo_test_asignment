from django.contrib import admin
from django.urls import path

from .views import RegistrationTemplateView, LoginTemplateView

urlpatterns = [
    path('signup/', RegistrationTemplateView.as_view(), name='registration'),
    path('signin/', LoginTemplateView.as_view(), name='login')
]
