from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Contact model.
    Defines how the Contact model is displayed in the Django admin panel.
    """
    
    # Specifies the fields to be displayed in the list view
    list_display = ('name', 'last_name', 'email', 'phone', 'message')

# Register the Contact model with its custom admin configuration
admin.site.register(Contact, ContactAdmin)
