from django import forms

class StudentRegistrationForm(forms.Form):
    # Dropdown choice field to select class and grade
    student_class = forms.ChoiceField(
        choices=[
            ('seven_one', 'پایه ۷ - یک'),
            ('seven_two', 'پایه ۷ - دو'),
            ('eight_one', 'پایه ۸ - یک'),
            ('eight_two', 'پایه ۸ - دو'),
            ('nine_one', 'پایه ۹ - یک'),
            ('nine_two', 'پایه ۹ - دو'),
        ],
        required=True,
        label='پایه و بخش'
    )

    # Student's login username
    username = forms.CharField(
        max_length=150,
        required=True,
        label='نام کاربری'
    )

    # Student's login password (masked input)
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label='رمز عبور'
    )

    # Father's full name
    father_name = forms.CharField(
        max_length=150,
        required=True,
        label='نام پدر'
    )

    # Father's phone number
    father_Phone = forms.CharField(
        max_length=20,
        required=True,
        label='تلفن پدر'
    )

    # Mother's phone number
    Mother_Phone = forms.CharField(
        max_length=20,
        required=True,
        label='تلفن مادر'
    )

    # Date of birth (as string, can be customized later with proper DateField)
    born = forms.CharField(
        max_length=50,
        required=True,
        label='تاریخ تولد'
    )

    # Full name of the student
    name = forms.CharField(
        max_length=150,
        required=True,
        label='نام'
    )

    # Student number, must be between 1 and 30
    class_number = forms.IntegerField(
        min_value=1,
        max_value=30,
        required=True,
        label='شماره دانش‌آموزی (۱ تا ۳۰)'
    )

    # Student's profile photo
    photo = forms.ImageField(
        required=True,
        label='عکس'
    )