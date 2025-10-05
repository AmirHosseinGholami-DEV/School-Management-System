from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Seven_Teacher_One, Seven_Teacher_Two, 
    Eight_Teacher_One, Eight_Teacher_Two, 
    Nine_Teacher_One, Nine_Teacher_Two
)

# 📌 **Base Admin Class for Managing Teachers**
class TeacherAdmin(admin.ModelAdmin):
    """
    A generic admin class to handle teacher models for different grades.
    This reduces code repetition and makes it easier to manage multiple teacher models.
    """
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    # 🖼️ **Method to Display Teacher's Photo in the Admin Panel**
    def display_photo(self, obj):
        """
        Displays a small thumbnail of the teacher's profile picture.
        If no photo is available, it returns 'No Photo'.
        """
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    
    display_photo.short_description = 'Photo'  # Column title in the admin panel

    # 🔑 **Method to Hide the Password for Security Reasons**
    def password_display(self, obj):
        """
        Displays masked password (*****) instead of the actual password 
        to maintain security in the admin panel.
        """
        return '********'
    
    password_display.short_description = 'Password'  # Column title in the admin panel

# 📌 **Registering All Teacher Models Using the Generic TeacherAdmin Class**
admin.site.register(Seven_Teacher_One, TeacherAdmin)
admin.site.register(Seven_Teacher_Two, TeacherAdmin)
admin.site.register(Eight_Teacher_One, TeacherAdmin)
admin.site.register(Eight_Teacher_Two, TeacherAdmin)
admin.site.register(Nine_Teacher_One, TeacherAdmin)
admin.site.register(Nine_Teacher_Two, TeacherAdmin)