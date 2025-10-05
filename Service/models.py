from django.db import models  # Import necessary module for defining models in Django

class Service(models.Model):
    # Field to store the name of the service, with a maximum length of 100 characters
    service_name = models.CharField(max_length=100)

    # Field to store the description of the service
    service_description = models.TextField()

    # String representation of the Service object, displayed when the object is printed or represented in Django admin
    def __str__(self):
        # Returning the service name to represent the object clearly in Django admin or shell
        return self.service_name

    # Optional: You can add custom methods to this model if needed.
    # For example, a method to display a shortened description:
    # def short_description(self):
    #     return self.service_description[:50] + "..."  # Returns the first 50 characters of the description

