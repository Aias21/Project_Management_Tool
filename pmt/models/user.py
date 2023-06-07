from django.db import models


class User(models.Model):
    ROLES = (
        ('A', 'Admin'),
        ('M', 'Manager'),
        ('E', 'Employee'),
        ('C', 'Customer'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=ROLES)
