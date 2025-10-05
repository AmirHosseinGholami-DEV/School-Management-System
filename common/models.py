from django.db import models

class Common(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email