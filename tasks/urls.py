from django.urls import path

from .views import IndexTemplateView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index_page'),
    path('tasks/', TaskCreateView.as_view(), name='tasks'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='update_task'),
]
