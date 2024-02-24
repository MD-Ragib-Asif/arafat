from django.urls import path
from .views import transaction_view

urlpatterns = [
    path('create_transaction/', transaction_view, name='create_transaction'),
    # Add other URLs as needed
]
