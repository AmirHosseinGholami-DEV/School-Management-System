from django.contrib import admin
from .models import (
    Fizik, Shimi, Zist,
    Math, Farsi, Emla,
    Negaresh, English,
    Arabic, Quran, Maref,
    Kar_Fan, Computer, Motaleat,
    Amadegi, Farhang_Honar, Varzesh
)

class LessonAdmin(admin.ModelAdmin):
    """ Admin panel configuration for all subjects. """
    list_display = ['name', 'month', 'score']

# Register all models using a loop
subjects = [
    Fizik, Shimi, Zist, Math, Farsi, Emla,
    Negaresh, English, Arabic, Quran, Maref,
    Kar_Fan, Computer, Motaleat, Amadegi, Farhang_Honar, Varzesh
]

for subject in subjects:
    admin.site.register(subject, LessonAdmin)