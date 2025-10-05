from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import StudentRegistrationForm
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from Staff.models import Staff
from Teacher.models import (
    Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One,
    Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two
)
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)
from Admin.models import Admin_Web

# View for handling user login
class LoginView(View):
    """Handles user login requests."""

    def get(self, request):
        """Render the login page on GET request."""
        return render(request, 'registration/login.html')

    def post(self, request):
        """Authenticate user and redirect based on role on POST request."""
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'لطفاً همه فیلدها را پر کنید.')
            return render(request, 'registration/login.html')

        # Define role-based models
        role_models = {
            'teacher': [
                Seven_Teacher_One, Seven_Teacher_Two, 
                Eight_Teacher_One, Eight_Teacher_Two, 
                Nine_Teacher_One, Nine_Teacher_Two
            ],
            'student': [
                Seven_Student_One, Seven_Student_Two, 
                Eight_Student_One, Eight_Student_Two, 
                Nine_Student_One, Nine_Student_Two
            ],
            'management': [Staff],
            'admin': [Admin_Web]
        }

        # Iterate over roles and check if the user exists
        for role, models in role_models.items():
            for model in models:
                if model.objects.filter(username=username, password=password).exists():
                    user = authenticate(request, username=username, password=password)
                    
                    if user is None:
                        user = User.objects.create_user(username=username, password=password)
                    
                    login(request, user)
                    return redirect(role)

        # If no user was found
        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        return render(request, 'registration/login.html')


# A dictionary to map student class string keys to their corresponding Django model classes
STUDENT_CLASS_MODEL_MAP = {
    'seven_one': Seven_Student_One,
    'seven_two': Seven_Student_Two,
    'eight_one': Eight_Student_One,
    'eight_two': Eight_Student_Two,
    'nine_one': Nine_Student_One,
    'nine_two': Nine_Student_Two,
}

class StudentRegisterView(View):
    template_name = "registration/registration.html"

    def get(self, request):
        """
        Handles GET request.
        Renders the registration form to the user.
        """
        form = StudentRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handles POST request.
        Validates the submitted form and saves the student data into the corresponding model
        based on the selected class.
        """
        form = StudentRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            # Extracting cleaned data from the form
            student_class = form.cleaned_data['student_class']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            father_name = form.cleaned_data['father_name']
            father_phone = form.cleaned_data['father_Phone']
            mother_phone = form.cleaned_data['Mother_Phone']
            born = form.cleaned_data['born']
            name = form.cleaned_data['name']
            class_number = form.cleaned_data['class_number']
            photo = form.cleaned_data['photo']

            # Get the appropriate model class based on selected student_class
            model = STUDENT_CLASS_MODEL_MAP.get(student_class)

            if model:
                # Check if the class_number is already taken in that class
                if model.objects.filter(class_number=class_number).exists():
                    # Show error message if student number is already used
                    messages.error(request, f"شماره دانش‌آموزی {class_number} قبلاً استفاده شده است.")
                else:
                    # Save the new student to the appropriate class model
                    model.objects.create(
                        username=username,
                        password=password,  # Note: Consider hashing password if this is used for login
                        father_name=father_name,
                        father_Phone=father_phone,
                        Mother_Phone=mother_phone,
                        born=born,
                        name=name,
                        class_number=class_number,
                        photo=photo
                    )
                    # Show success message and redirect to login page
                    messages.success(request, "ثبت‌نام با موفقیت انجام شد.")
                    return redirect("login")
            else:
                # Invalid student_class selected (not found in the map)
                messages.error(request, "کلاس انتخاب‌شده نامعتبر است.")
        else:
            # Form validation failed (missing or invalid fields)
            messages.error(request, "فرم دارای خطاست. لطفاً فیلدها را بررسی کنید.")

        # Render the form again with error messages
        return render(request, self.template_name, {'form': form})
