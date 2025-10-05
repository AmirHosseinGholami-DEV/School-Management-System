from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Seven_Student_One, Seven_Student_Two, 
    Eight_Student_One, Eight_Student_Two, 
    Nine_Student_One, Nine_Student_Two
)

# Base class for student admin with common behavior
class Student_Admin(admin.ModelAdmin):
    ordering = ['class_number']

    # Common fields for displaying in the list view
    list_display = ('name', 'username','class_number', 'father_name', 'display_photo', 'password_display', 'father_Phone', 'class_number', 'Mother_Phone')

    # Custom method to display the student's photo in the admin list view
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"  # If there's no photo, display "No Photo"
    display_photo.short_description = 'Photo'  # Label to display in the admin interface

    # Custom method to display the password as masked text (avoid exposing the real password)
    def password_display(self, obj):
        return '********'  # Masked password to prevent exposure
    password_display.short_description = 'Password'  # Label to display in the admin interface


# Register each model with the admin interface using the base class
admin.site.register(Seven_Student_One, Student_Admin)
admin.site.register(Seven_Student_Two, Student_Admin)
admin.site.register(Eight_Student_One, Student_Admin)
admin.site.register(Eight_Student_Two, Student_Admin)
admin.site.register(Nine_Student_One, Student_Admin)
admin.site.register(Nine_Student_Two, Student_Admin)
