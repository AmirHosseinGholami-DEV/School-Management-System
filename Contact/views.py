from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import ContactForm  # اصلاح نام فرم برای مطابقت با استانداردهای نام‌گذاری

class ContactView(TemplateView):
    """
    View to handle the contact form.
    Uses a TemplateView to render the contact page and handle form submissions.
    """
    template_name = 'Contact Page/Contact.html'  # Define the template to be used

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the template.
        """
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactForm()  # Add an empty form to the context
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles form submission.
        Validates the form and either saves it or returns errors.
        """
        contact_form = ContactForm(request.POST, request.FILES)

        if contact_form.is_valid():
            contact_form.save()
            return redirect("Contact Page")  # Redirect to the contact page after successful submission

        # If the form is not valid, re-render the page with error messages
        return self.render_to_response(self.get_context_data(contact=contact_form))
