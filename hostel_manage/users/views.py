from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserEx
# from .forms import UserForm


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
        phone = request.POST['phone']
        sex = request.POST['sex']
        role = request.POST['role']

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

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        current_user = request.user

        username = request.POST.get('username')
        user_instance = User.objects.get(username=username)
        print(f"User__Instance: {user_instance}")
        user_ex = UserEx.objects.create(user=user_instance)
        print(f"user ex create: {user_ex}")

        # user_ex = UserEx.objects.create(u
        # user_ex.user_name = username
        user_ex.phone = phone
        user_ex.sex = sex
        user_ex.role = role
        myuser.is_active = True
        myuser.save()
        user_ex.save()
        messages.success(request, "Your Account has been created successfully!!")

        # # Welcome Email
        # subject = "Welcome to GFG- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + ("Welcome to GFG!! \nThank you for visiting our website\n. "
        #                                                     "We have also sent you a confirmation email, "
        #                                                     "please confirm your email address. \n\nThanking "
        #                                                     "You\nAnubhav Madhav")
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        #
        # # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ GFG - Django Login!!"
        # message2 = render_to_string('email_confirmation.html', {
        #
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

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