from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Suggestions
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def suggestion_view(request, *args, **kargs):
    if request.method == 'POST':
        content = request.POST.get('content')
        suggestion = Suggestions(
            content=content,
            user=request.user,
            dt=str(timezone.now())
        )
        suggestion.save()
        return redirect('suggestion_view')

    all_suggs = Suggestions.objects.all()
    # username = request.user.username
    # role = User.objects.filter(username=username).values_list('role', flat=True)
    # print(role)
    su = request.user.is_superuser
    role = ''
    if su:
        role = 'Manager'
    else:
        role = 'Member'
    sugg_context = {
        'all': all_suggs,
        'role_choice': role
    }
    return render(request, 'suggestions/suggestion.html', sugg_context)
