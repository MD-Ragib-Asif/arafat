from django.shortcuts import render, redirect
from .models import Account, Transaction
from decimal import Decimal


# forms.py file for forms

def transaction_view(request):  # data receive
    if request.method == 'POST':
        amount = request.POST['amount']
        tran_type = request.POST['tran_type']
        user = request.user
        # account   = user.account
        transaction = Transaction(
            amount=amount,
            tran_type=tran_type,
            user=user,
            # account_id=account
        )
        transaction.save()
        print(amount)
        account = Account.objects.get(id=1)
        print(account.Total_balance)
        print('________', tran_type, '________-')
        if str(tran_type) == 'Deposit':
            account.Total_balance += Decimal(amount)
        else:
            account.Total_balance -= Decimal(amount)
        # account_updated= Account(
        #     Total_balance = account.Total_balance
        # )
        account.save()
        print(account.Total_balance)
        print(f"DEBUG: {account=}")
        return render(request, "users/index.html")
    su = request.user.is_superuser
    role = ''
    if su:
        role = 'Manager'
    else:
        role = 'Member'
    print('=============================', role, '==============================')
    tran_context = {
        'role_choice': role
    }

    return render(request, 'transaction/transaction.html', tran_context)


def account_view(request):
    name = request.user.username
    su = request.user.is_superuser
    i_d = request.user.id
    print(i_d, '============================')
    account = Account.objects.get(id=1)
    total_balance = account.Total_balance
    total_balance = str(total_balance)
    print('===============================',
          'name', name, "su", su, 'total _bal', total_balance,
          '======================================'
          )

    account_context = {
        "name": name,
        "su": su,
        "balance": total_balance
    }
    return render(request, 'transaction/accounts.html', account_context)
