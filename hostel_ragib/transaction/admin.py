from django.contrib import admin

# Register your models here.
from .models import Account, Transaction

class TransactionView(admin.ModelAdmin):
    list_display = [
        '__str__',
        'type',
        'amount'
    ]
class AccountView(admin.ModelAdmin):
    list_display = [
        '__str__',
        'Total_balance'
    ]

admin.site.register(Account, AccountView)
admin.site.register(Transaction, TransactionView)