from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "users/index.html")


def signup(request):
    if request.method == "POST":

        print(f"====== {request.POST=}")
        username = request.POST['username']
        print(f"Username Instance: {username}")
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        role = request.POST['is_superuser']
        if role == 'Member':
            role = 0
        else:
            role = 1

        if pass1 != pass2:
            messages.error(request, "Password didn't match")
            return redirect('home')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username=username, email=email, password=pass1, is_superuser=role)
        myuser.first_name = fname
        myuser.last_name = lname
        username = request.POST.get('username')
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created successfully!!")
        return redirect('signin')

    return render(request, "users/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        print(f'============== {username} {pass1} ==============')

        user = authenticate(username=username, password=pass1)
        print("User:", user)

        if user is not None:

            login(request, user)
            fname = user.first_name
            lname = user.last_name
            # messages.success(request, "Logged In Successfully!!")
            return render(request, "users/index.html", {"fname": fname, "lname": lname})
        else:

            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "users/signin.html")


def signout(request):
    print(f"Request: {request}")
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
