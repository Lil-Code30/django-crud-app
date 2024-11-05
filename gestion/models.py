from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=6)
    position = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
