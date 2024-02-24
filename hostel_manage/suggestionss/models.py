from django.db import models

from django.contrib.auth.models import User


class Suggestions(models.Model):
    sugg_id = models.AutoField(primary_key=True, null=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dt = models.TextField(default='12')
