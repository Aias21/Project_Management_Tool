from django.db import models
from pmt.models.user import User


class Admin(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)