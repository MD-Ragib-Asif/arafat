from django.shortcuts import render
from django.utils import timezone
from .models import Chat
from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request, *args, **kargs):
    if request.method == 'POST':
        content = request.POST.get('content')
        # username= request.POST.get("username")
        print(timezone.now())
        dt = str(timezone.now())
        chat = Chat(
            content=content,
            user=request.user,
            dt=str(timezone.now())
        )
        chat.save()
    chats = Chat.objects.all()
    chat_context = {
        'all': chats[len(chats) - 8:len(chats)]  # That gives error If we have less than 8 Chat Contents
    }
    return render(request, 'chats/chats.html', chat_context)
