from django.urls import path
from .views import transaction_view,account_view

urlpatterns = [
    path('transaction_view/', transaction_view, name='transaction_view'),
    path('account_view/', account_view, name='account_view')
]
