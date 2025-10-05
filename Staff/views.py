from django.views.generic import TemplateView  # Importing TemplateView from Django to render HTML templates
from .models import Staff  # Importing the Staff model from the current app's models

class Staff_View(TemplateView):
    # Define the template to be used to render the page
    template_name = 'Staff List/index.html'

    # Overriding the get_context_data method to pass custom data to the template
    def get_context_data(self, **kwargs):
        # Calling the parent class's get_context_data method to retain any default context data
        context = super().get_context_data(**kwargs)

        # Adding a custom context key 'Staff' which contains all staff members from the database
        context['Staff'] = Staff.objects.all()  # Query all Staff objects and pass them to the template context

        # Returning the context with the staff data to be used in the template
        return context
