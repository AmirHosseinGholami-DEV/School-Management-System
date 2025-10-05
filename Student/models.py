from django.db import models  # Importing the necessary module for defining models in Django
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    # Common fields for all students
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    class_number = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(30)
        ],
        verbose_name='Student Number'
    )

    class Meta:
        # Abstract base class to avoid creating a table for this class
        abstract = True

    def __str__(self):
        return self.username


# Now, instead of creating multiple classes, we can inherit from the base 'Student' class.

class Seven_Student_One(Student):
    # This class will represent "Seven Student One" and inherit from the base Student class
    pass


class Seven_Student_Two(Student):
    # This class will represent "Seven Student Two" and inherit from the base Student class
    pass


class Eight_Student_One(Student):
    # This class will represent "Eight Student One" and inherit from the base Student class
    pass


class Eight_Student_Two(Student):
    # This class will represent "Eight Student Two" and inherit from the base Student class
    pass


class Nine_Student_One(Student):
    # This class will represent "Nine Student One" and inherit from the base Student class
    pass


class Nine_Student_Two(Student):
    # This class will represent "Nine Student Two" and inherit from the base Student class
    pass
