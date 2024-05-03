from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    desc = models.CharField(max_length=50)