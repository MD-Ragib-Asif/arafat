from django.contrib import admin
from django.urls import path, include
from .views import (signin_view, signup_view, signout_view, home_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('home', home_view, name='home'),
    path('signup', signup_view, name='signup'),
    path('signin', signin_view, name='signin'),
    path('signout', signout_view, name='signout'),
]
