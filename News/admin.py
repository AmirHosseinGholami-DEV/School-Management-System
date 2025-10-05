from django.contrib import admin
from .models import News
# Register your models here.

class News_Admin(admin.ModelAdmin):
    list_display = ('subject', 'description', 'photo')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'

admin.site.register(News, News_Admin)