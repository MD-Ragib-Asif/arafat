from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('chat/', include('chat.urls')),
    path('suggestions/', include('suggestionss.urls')),
    path('transactions/', include('transaction.urls')),
    path('notifications/', include('notification.urls')),
    path('meal/', include('meal.urls')),
]
