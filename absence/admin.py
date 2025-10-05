from django.contrib import admin
from .models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)

# Base admin configuration for absence models
class BaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'lessone']  # Keeping original field names

# List of absence models to register
absence_models = [
    Seven_One_Absence, Seven_Two_Absence, 
    Eight_One_Absence, Eight_Two_Absence, 
    Nine_One_Absence, Nine_Two_Absence
]

# Register all absence models using a loop for cleaner code
for model in absence_models:
    admin.site.register(model, BaseAdmin)
