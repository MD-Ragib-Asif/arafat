from django.db import models
from users.models import UserEx
from django.contrib.auth.models import User

import datetime


# Create your models here.
class Chat(models.Model):
    conv_id = models.AutoField(primary_key=True, null=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dt = models.TextField(default='12')
