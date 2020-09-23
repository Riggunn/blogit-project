
# view.py -- accounts
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib import messages

# Create your views here.
def login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'accounts/login.html', context=context)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back, {}!'.format(user.username))
            return redirect('index') 
        else:
            messages.error(request, 'Username or Password is incorrect')
            return render(request, 'accounts/login.html', context=context)

def register(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'accounts/register.html', context=context)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
            except:
                messages.error(request, 'Something going wrong... Please, try again...')
                return render(request, 'accounts/register.html', context=context)
            else:
                auth.login(request, user)
                messages.success(request, '{}, you have been registered successfully! Fill your profile details now or you can do it later!'.format(user.username))
                return redirect('/profiles/profile/{}'.format(user.username))
        else:
            messages.error(request, 'Password and Confirm Password is not match... Please, try again...')
            return render(request, 'accounts/register.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('login')