from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Form for the Contact model.
    Provides validation to ensure all required fields are filled.
    """

    class Meta:
        model = Contact  # Specify the model associated with this form
        fields = ['name', 'last_name', 'email', 'phone', 'message']  # Define the fields to include in the form

    def clean(self):
        """
        Custom form validation method.
        Ensures that all required fields are filled before submission.
        """
        cleaned_data = super().clean()  # Get cleaned data from the form

        # Extract form fields
        name = cleaned_data.get("name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        # Validate that none of the required fields are empty
        if not all([name, last_name, email, phone, message]):
            raise forms.ValidationError("Please fill in all required contact fields.")

        return cleaned_data  # Return the cleaned data
