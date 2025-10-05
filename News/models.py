from django.db import models

class News(models.Model):
    subject = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.subject