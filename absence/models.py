from django.db import models

# Base model for absence records
class AbsenceBase(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)
    shamsi_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True  # This makes it an abstract model (not created as a table)

    def __str__(self):
        return f"{self.name} - ({self.shamsi_date}):: {self.lessone}"

# Subclasses for different grades and sections
class Seven_One_Absence(AbsenceBase):
    pass

class Seven_Two_Absence(AbsenceBase):
    pass

class Eight_One_Absence(AbsenceBase):
    pass

class Eight_Two_Absence(AbsenceBase):
    pass

class Nine_One_Absence(AbsenceBase):
    pass

class Nine_Two_Absence(AbsenceBase):
    pass
