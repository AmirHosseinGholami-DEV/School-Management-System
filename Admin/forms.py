from django import forms
from News.models import News
from Staff.models import Staff
from Service.models import Service
from Facilities.models import Facilities
from Student.models import (
    Seven_Student_One, Seven_Student_Two,
    Eight_Student_One, Eight_Student_Two,
    Nine_Student_One, Nine_Student_Two
)
from Teacher.models import (
    Seven_Teacher_One, Seven_Teacher_Two,
    Eight_Teacher_One, Eight_Teacher_Two,
    Nine_Teacher_One, Nine_Teacher_Two
)


# Base form class for student forms to avoid redundancy
class BaseStudentForm(forms.ModelForm):
    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError(f"Please fill in all required fields for {self.Meta.model.__name__}.")
        
        return cleaned_data


# Student Forms
class Seven_Student_One_Form(BaseStudentForm):
    class Meta:
        model = Seven_Student_One
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


class Seven_Student_Two_Form(BaseStudentForm):
    class Meta:
        model = Seven_Student_Two
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


class Eight_Student_One_Form(BaseStudentForm):
    class Meta:
        model = Eight_Student_One
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


class Eight_Student_Two_Form(BaseStudentForm):
    class Meta:
        model = Eight_Student_Two
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


class Nine_Student_One_Form(BaseStudentForm):
    class Meta:
        model = Nine_Student_One
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


class Nine_Student_Two_Form(BaseStudentForm):
    class Meta:
        model = Nine_Student_Two
        fields = ['class_number', 'name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']


# Base form class for teacher forms to avoid redundancy
class BaseTeacherForm(forms.ModelForm):
    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError(f"Please fill in all required fields for {self.Meta.model.__name__}.")
        
        return cleaned_data


# Teacher Forms
class Seven_Teacher_One_Form(BaseTeacherForm):
    class Meta:
        model = Seven_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


class Seven_Teacher_Two_Form(BaseTeacherForm):
    class Meta:
        model = Seven_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


class Eight_Teacher_One_Form(BaseTeacherForm):
    class Meta:
        model = Eight_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


class Eight_Teacher_Two_Form(BaseTeacherForm):
    class Meta:
        model = Eight_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


class Nine_Teacher_One_Form(BaseTeacherForm):
    class Meta:
        model = Nine_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


class Nine_Teacher_Two_Form(BaseTeacherForm):
    class Meta:
        model = Nine_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']


# Staff Form
class Staff_Form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'username', 'password', 'staff', 'phone_number', 'photo']

    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['name', 'username', 'password', 'staff', 'phone_number', 'photo']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError("Please fill in all required fields for Staff.")
        
        return cleaned_data


# News Form
class News_Form(forms.ModelForm):
    class Meta:
        model = News
        fields = ['subject', 'description', 'photo']

    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['subject', 'description', 'photo']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError("Please fill in all required fields for News.")
        
        return cleaned_data


# Facilities Form
class Facilities_Form(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['name', 'photo']

    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['name', 'photo']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError("Please fill in all required fields for Facilities.")
        
        return cleaned_data


# Service Form
class Service_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description']

    def clean(self):
        """
        Validates that all required fields are filled.
        Raises a ValidationError if any required field is missing.
        """
        cleaned_data = super().clean()
        required_fields = ['service_name', 'service_description']
        
        for field in required_fields:
            if not cleaned_data.get(field):
                raise forms.ValidationError("Please fill in all required fields for Service.")
        
        return cleaned_data