from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=500)
    relationship = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name