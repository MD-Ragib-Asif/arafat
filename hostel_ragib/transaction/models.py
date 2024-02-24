from django.db import models
from users.models import User 

# Create your models here.
class Account(models.Model):
    Total_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=False)
    def __str__(self):
        return f'Account {self.id}'
 

class Transaction(models.Model):
    Transaction_types = [
        ('withdraw', 'Withdraw'),
        ('deposite', 'Deposite'),
    ]
    # transtion_id = models.AutoField()
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.CharField(max_length=10, choices=Transaction_types)
    # history = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="transaction"

    def __str__(self):
        return f'Transaction done by {self.user_name}'