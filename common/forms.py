from django import forms
from .models import Common

class Common_Form(forms.ModelForm):
    """
    Form for the Common model.
    Provides validation for the email field.
    """
    
    class Meta:
        model = Common  # Specify the model associated with this form
        fields = ['email']  # Define the fields to include in the form

    def clean(self):
        """
        Custom form validation method.
        Ensures that the email field is not empty.
        """
        cleaned_data = super().clean()  # Get cleaned data from the form
        email = cleaned_data.get("email")

        # Validate that the email field is not empty
        if not email:
            raise forms.ValidationError("Please fill in the required subscription field.")

        return cleaned_data  # Return the cleaned data
