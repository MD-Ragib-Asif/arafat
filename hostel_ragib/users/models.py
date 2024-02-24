from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, null=False, primary_key=True,)
    password = models.CharField(max_length=20, null=False, default='123')
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=14, null=False)  # +8801827556515
    user_type = models.CharField(default='Member', max_length=10, null=False)  # Manager or Member Apatoto Char (Option Choose korar system hobe)
    hostel_id = models.CharField(max_length=10, null=False)  # Apatoto Char (Option Choose korar system hobe)


    class Meta:
        db_table = "user"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"