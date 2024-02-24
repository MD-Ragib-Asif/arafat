from django.db import models
from django.contrib.auth.models import User

'''
CREATE TABLE `transaction` (`id` bigint AUTO_INCREMENT NO
T NULL PRIMARY KEY, `amount` numeric(10, 2) NOT NULL, `ty
pe` varchar(10) NOT NULL, `time` datetime(6) NOT NULL, `a
ccount_id_id` bigint NOT NULL, `user_name_id` integer NOT
 NULL);
ALTER TABLE `transaction_account` ADD CONSTRAINT `transac
tion_account_user_name_id_a2d18b0b_fk_auth_user_id` FOREI
GN KEY (`user_name_id`) REFERENCES `auth_user` (`id`);   
ALTER TABLE `transaction` ADD CONSTRAINT `transaction_acc
ount_id_id_e6bb711e_fk_transaction_account_id` FOREIGN KE
Y (`account_id_id`) REFERENCES `transaction_account` (`id
`);
ALTER TABLE `transaction` ADD CONSTRAINT `transaction_use
r_name_id_dfc050c1_fk_auth_user_id` FOREIGN KEY (`user_na
me_id`) REFERENCES `auth_user` (`id`);

'''

class Account(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    Total_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=False)

    def __str__(self):
        return f'Account {self.id}'


# account for future


class Transaction(models.Model):
    Transaction_types = [
        ('withdraw', 'Withdraw'),
        ('deposite', 'Deposite'),
    ]
    # transtion_id = models.AutoField()
    # account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tran_type = models.CharField(max_length=10, choices=Transaction_types)
    # history = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transaction"

    def __str__(self):
        return f'Transaction done by {self.user_name}'
