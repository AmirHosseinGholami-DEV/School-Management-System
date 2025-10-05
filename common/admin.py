from django.contrib import admin
from .models import Common

# Define a custom admin class for the Common model
class CommonAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Common model.
    This class controls how the model is displayed in the Django admin panel.
    """
    
    # Specifies the fields to be displayed in the list view
    list_display = ('email',)

# Register the Common model with its custom admin configuration
admin.site.register(Common, CommonAdmin)
