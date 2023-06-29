from django.contrib import admin
from django.urls import path

from .views import IndexTemplateView, TaskCreateView, TaskDeleteView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index_page'),
    path('tasks/', TaskCreateView.as_view(), name='tasks'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='delete_task')
]
