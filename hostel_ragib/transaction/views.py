from django.shortcuts import render, redirect
from .models import Account, Transaction
from .forms import TransactionForm  # forms.py file for forms

def transaction_view(request): #data receive
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Process and save the form data to the database
            form.save()
            return redirect('transaction_success')  # Redirect to a success page
    else:
        form = TransactionForm()

    return render(request, 'transaction.html', {'form': form})
