from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError
from django.urls import reverse


def HomePage(request):
    return render(request,'home.html')



def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phonenumber')
        passw = request.POST.get('password')

        try:
            # create a new user
            new_user = User.objects.create_user(username=uname, email=email, password=passw)
            new_user.save()
            return redirect('login')
        except IntegrityError:
            # where the username is not unique
            error_message = "Username is already taken. Please choose a different username."
            signup_url = reverse('signup') 
            return render(request, 'signUp.html', {'error_message': error_message, 'signup_url': signup_url})

    return render(request, 'signup.html')



def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'main.html', {'error_message': error_message})

    return render(request, 'main.html')



def forgot_password(request):
    return render(request,'forgetPass.html')
