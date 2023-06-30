from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Task model.

    This class configures the representation of the Task model in the Django Admin panel.
    It customizes the list view of Task objects, displaying specific fields in the list display.

    Attributes:
        list_display (tuple): A tuple containing the names of fields to be displayed in the list view.

    """
    list_display = ('id', 'title', 'status',)
