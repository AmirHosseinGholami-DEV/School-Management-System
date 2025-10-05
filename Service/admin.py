# Importing necessary modules from Django
from django.contrib import admin
from .models import Service  # Import the Service model from the current app's models

# Customizing the admin interface for the Service model
class ServiceAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = ('service_name', 'service_description')

    # Optional: You can add additional customization methods here, e.g., search fields, filters, etc.
    # search_fields = ['service_name', 'service_description']  # Uncomment to add search functionality
    # list_filter = ['service_name']  # Uncomment to add filter options by service_name

# Register the Service model with the customized admin interface
admin.site.register(Service, ServiceAdmin)
