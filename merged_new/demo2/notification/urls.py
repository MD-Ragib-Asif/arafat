from django.urls import path
from . import views

urlpatterns = [
    path('create_notification/', views.create_notification, name='create_notification'),
    path('notifications/', views.notification_list, name='notification_list'),
    # Add other URLs as needed
]
