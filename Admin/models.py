from django.db import models

class Admin_Web(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username