from django.contrib import admin
from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogout

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='registration'),
    path('signin/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout')
]
