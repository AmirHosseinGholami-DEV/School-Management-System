from django.contrib import admin
from django.utils.html import format_html
from .models import Admin_Web  # Importing the Admin_Web model

class AdminWebAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Admin_Web model.
    This class customizes the display of the Admin_Web model in the Django admin interface.
    """

    # Defining the fields to be displayed in the admin list view
    list_display = ('name', 'username', 'phone_number', 'display_photo', 'password_display')

    def display_photo(self, obj):
        """
        This method returns an HTML image tag to display the admin's profile photo.
        If the admin has uploaded a photo, it will be displayed as a small image.
        If no photo is available, it returns 'No Photo'.
        """
        if obj.photo and hasattr(obj.photo, 'url'):
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return "No Photo"

    # Setting the column name for the display_photo method in the admin panel
    display_photo.short_description = 'Photo'

    def password_display(self, obj):
        """
        This method hides the password field in the admin panel by displaying asterisks (********).
        This ensures that the actual password is not visible for security reasons.
        """
        return '********'

    # Setting the column name for the password_display method in the admin panel
    password_display.short_description = 'Password'

# Registering the Admin_Web model with its custom admin configuration
admin.site.register(Admin_Web, AdminWebAdmin)
