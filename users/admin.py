from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin model configuration for CustomUser.

    This class is used to customize the appearance and functionality of the CustomUser model
    in the Django admin interface. It specifies the fields to be displayed in the list view.

    Attributes:
        list_display (tuple): A tuple containing the names of fields to be displayed in the list view.

    """
    list_display = ('id', 'email', 'is_staff')
