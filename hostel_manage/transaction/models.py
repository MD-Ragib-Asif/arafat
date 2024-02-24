from django.db import models


# from users.views import

# Create your models here.
class Account(models.Model):

    def __str__(self):
        return f'Account {self.id}'


class Transaction(models.Model):
    Transaction_types = [
        ('withdraw', 'Withdraw'),
        ('deposite', 'Deposite'),
    ]

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=Transaction_types)
    # history = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.id} - {self.type} - {self.amount}'
