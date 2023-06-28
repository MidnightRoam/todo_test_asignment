from django.contrib import admin
from django.urls import path

from .views import IndexTemplateView, TaskListView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index_page'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
]
