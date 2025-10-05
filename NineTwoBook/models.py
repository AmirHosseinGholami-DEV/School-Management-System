from django.db import models

class Subject(models.Model):
    """
    Abstract base model for different subjects.
    Stores student name, month, and score.
    """
    name = models.CharField(max_length=100)  # Student's name
    month = models.CharField(max_length=50)  # The month of evaluation
    score = models.CharField(max_length=10)  # Score for the subject

    class Meta:
        abstract = True  # This makes the model abstract (not stored in the database)

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"


# Child models for each subject, preserving the original names
class Fizik(Subject): pass
class Shimi(Subject): pass
class Zist(Subject): pass
class Math(Subject): pass
class Farsi(Subject): pass
class Emla(Subject): pass
class Negaresh(Subject): pass
class English(Subject): pass
class Arabic(Subject): pass
class Quran(Subject): pass
class Maref(Subject): pass
class Kar_Fan(Subject): pass 
class Computer(Subject): pass
class Motaleat(Subject): pass
class Amadegi(Subject): pass
class Farhang_Honar(Subject): pass
class Varzesh(Subject): pass