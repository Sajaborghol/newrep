
from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    def __str__(self):
        return self.name
