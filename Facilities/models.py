from django.db import models

class Facilities(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name

