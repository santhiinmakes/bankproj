
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['password1']

        if password == conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('credentials:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User Created")
        else:
            messages.info(request, "password not matching")
            return redirect('credentials:register')
        return redirect('credentials:login')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dropdown:index')

        else:
            print("invalid user")
            messages.info(request, 'invalid credentials')
            return redirect('credentials:login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
