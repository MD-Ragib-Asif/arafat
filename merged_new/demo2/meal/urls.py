# meal_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_meal, name='add_meal'),
    path('view/', views.view_meal_cost, name='view_meal_cost'),
]
