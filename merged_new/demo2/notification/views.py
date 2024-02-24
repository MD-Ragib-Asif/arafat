from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def create_notification(request):
    if not request.user.is_superuser:
        return redirect('notification_list')  # Redirect non-superusers to view notifications

    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        Notification.objects.create(user=request.user, title=title, message=message)
        messages.success(request, "Your Notification Uploaded Successfully!!")
        return render(request, "users/index.html")

    # Render a form for superusers to create notifications
    return render(request, 'notification/create_notification.html')


def notification_list(request):
    notifications = Notification.objects.all().order_by('-created_at')
    return render(request, 'notification/notification_list.html', {'notifications': notifications})
