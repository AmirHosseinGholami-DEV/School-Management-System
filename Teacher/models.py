from django.db import models

class BaseTeacher(models.Model):
    """
    Abstract base model for teachers.
    This model contains common fields for all teacher categories.
    """
    username = models.CharField(max_length=150, unique=True)  # Unique identifier for each teacher
    password = models.CharField(max_length=128)  # Hashed password storage
    name = models.CharField(max_length=100)  # Teacher's full name
    course = models.CharField(max_length=100)  # Course/Subject the teacher teaches
    phone_number = models.CharField(max_length=100)  # Contact number
    photo = models.ImageField(upload_to='photos/')  # Profile picture storage

    class Meta:
        abstract = True  # This model won't be created in the database

    def __str__(self):
        return self.name  # Returns the teacher's name in the admin panel


# Concrete teacher models inheriting from BaseTeacher
class Seven_Teacher_One(BaseTeacher):
    """Teachers for Grade 7, Section 1"""
    pass

class Seven_Teacher_Two(BaseTeacher):
    """Teachers for Grade 7, Section 2"""
    pass

class Eight_Teacher_One(BaseTeacher):
    """Teachers for Grade 8, Section 1"""
    pass

class Eight_Teacher_Two(BaseTeacher):
    """Teachers for Grade 8, Section 2"""
    pass

class Nine_Teacher_One(BaseTeacher):
    """Teachers for Grade 9, Section 1"""
    pass

class Nine_Teacher_Two(BaseTeacher):
    """Teachers for Grade 9, Section 2"""
    pass
