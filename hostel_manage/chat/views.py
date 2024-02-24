from django.shortcuts import render
from django.utils import timezone
from .models import Chat


def chat_view(request, *args, **kargs):
    if request.method == 'POST':
        content = request.POST.get('content')
        # username= request.POST.get("username")
        # print(timezone.now())
        dt = str(timezone.now())  # Date time String
        chat = Chat(
            content=content,
            user=request.user,
            dt=str(timezone.now())
        )
        chat.save()
    chats = Chat.objects.all()

    if len(chats) >= 8:
        chat_context = {
            'all': chats[len(chats) - 8:len(chats)]
        }
    else:
        chat_context = {
            'all': chats[0:len(chats)]
        }
    return render(request, 'chats/chats.html', chat_context)
