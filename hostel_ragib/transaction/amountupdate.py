from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_total_amount(sender, instance, **kwargs):
    if instance.type == 'withdraw':
        instance.account_id.Total_balance -= instance.amount
    else:
        instance.account_id.Total_balance += instance.amount

    # Save the updated Total_amount back to the account
    instance.account_id.save()