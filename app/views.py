from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, 'Email already exists')

        else:
            if request.POST['password'] != request.POST['repeat_password']:
                messages.warning(request, 'Passwords dont match')
            else:
                query = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST[
                    'username'], email=request.POST['email'], password=request.POST['password'])
                query.set_password(request.POST['password'])
                query.save()
                messages.success(request, 'User Created Successfully')
                return redirect(login)
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        if username != "" and password != "":
            query = authenticate(request, username=username, password=password)
            print(query)
            if query is None:
                messages.error(request, "Invalid Credentials")
            else:
                login(request, query)
                messages.success(request,'Welcome To BugBounty')
                return redirect(index)
        else:
            messages.warning(request, "Null Values are not allowed")
    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect(login_user)



def userprofile(request):
    return render(request, 'profile.html')
