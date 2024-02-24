from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('choice', views.transaction_view, name='transaction_views'),
]
