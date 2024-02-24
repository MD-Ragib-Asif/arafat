from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import UserForm


# Create your views here.
def home_view(request):
    return render(request, 'users/index.html', {})


def signup_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm(request.POST or None)

    context = {
        'form': form
    }

    # if User.objects.filter(username=username):
    #     messages.error(request, "Username already exist! Please try some other username.")
    #     return redirect('home')
    #
    # if User.objects.filter(email=email).exists():
    #     messages.error(request, "Email Already Registered!!")
    #     return redirect('home')
    #
    # if len(username) > 20:
    #     messages.error(request, "Username must be under 20 charcters!!")
    #     return redirect('home')
    #
    # if pass1 != pass2:
    #     messages.error(request, "Passwords didn't matched!!")
    #     return redirect('home')
    #
    # if not username.isalnum():
    #     messages.error(request, "Username must be Alpha-Numeric!!")
    #     return redirect('home')
    #
    # myuser = User.objects.create_user(username, email, pass1)
    # myuser.first_name = fname
    # myuser.last_name = lname
    # # myuser.is_active = False
    # myuser.is_active = False
    # myuser.save()
    # messages.success(request, "Your Account has been created successfully!!")
    # return redirect('signin')

    return render(request, "users/signup.html", context)


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        print(user)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "users/index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "users/signin.html")


def signout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/home')
