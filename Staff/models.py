from django.db import models  # Import necessary module for defining models in Django

class Staff(models.Model):
    # Field to store the username of the staff member, must be unique
    username = models.CharField(max_length=150, unique=True)

    # Field to store the password, typically hashed, so the max length is set to 128
    password = models.CharField(max_length=128)

    # Field to store the name of the staff member
    name = models.CharField(max_length=100)

    # Field to store the role or position of the staff member
    staff = models.CharField(max_length=120)

    # Field to store the phone number of the staff member
    phone_number = models.CharField(max_length=100)

    # Field to upload and store the staff member's photo in the 'photos/' directory
    photo = models.ImageField(upload_to='photos/')

    # String representation of the Staff object, returning the name of the staff member
    def __str__(self):
        # This method helps in representing the object in Django admin or shell by the staff member's name
        return self.name

    # Optional: You can add custom methods to this model as needed.
    # For example, a method to check if the staff member is active could be added here:
    # def is_active(self):
    #     return self.status == 'active'
