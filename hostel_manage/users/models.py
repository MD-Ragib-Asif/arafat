from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserEx(models.Model):
    sex_types = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    member_type = [
        ('manager', 'Manager'),
        ('member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    phone = models.CharField(max_length=15)
    sex = models.CharField(max_length=10, choices=sex_types)
    role = models.CharField(max_length=7, choices=member_type)

    def __str__(self):
        return self.user.username
