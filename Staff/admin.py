from django.contrib import admin  # Importing the admin module to customize the admin interface
from django.utils.html import format_html  # Importing format_html to format HTML output
from .models import Staff  # Importing the Staff model from the current app's models

class StaffAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view of the Staff model in the admin panel
    list_display = ('name', 'username', 'phone_number', 'staff', 'display_photo', 'password_display')

    # Custom method to display the photo of the staff member in the admin panel
    def display_photo(self, obj):
        if obj.photo:
            # If a photo is available, it will be displayed as an image with width and height set to 50px
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"  # If no photo is set, show a "No Photo" message
    display_photo.short_description = 'Photo'  # Label to display in the admin panel

    # Custom method to display a masked password (to avoid exposing the actual password)
    def password_display(self, obj):
        return '********'  # Show masked password
    password_display.short_description = 'Password'  # Label to display in the admin panel

# Register the Staff model with the customized admin interface
admin.site.register(Staff, StaffAdmin)
