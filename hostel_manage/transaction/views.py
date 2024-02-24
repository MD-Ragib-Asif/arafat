from django.shortcuts import render

# Create your views here.
from .models import Transaction, Account


def transaction_view(request):
    obj = Transaction.objects.get(id=1)

    context = {
        'object': obj
    }

    return render(request, 'transcation/choice.html', context)
