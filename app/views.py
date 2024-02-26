from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def index(request):
    data = Posts.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        data = Posts.objects.filter(Q(tags__icontains=name) | Q(
            title__icontains=name) | Q(description__icontains=name)| Q(user__username__icontains=name))

    paginator = Paginator(data, 6)
    page_number = request.GET.get('page')
    service_data = paginator.get_page(page_number)
    return render(request, 'index.html', {"query": service_data})


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).exists() or User.objects.filter(username=request.POST['username']).exists():
            messages.warning(request, 'Username / Email already exists')
        else:
            if request.POST['password'] != request.POST['repeat_password']:
                messages.warning(request, 'Passwords dont match')
            else:
                query = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST[
                    'username'], email=request.POST['email'], password=request.POST['password'])
                query.set_password(request.POST['password'])
                query.save()
                messages.success(request, 'User Created Successfully')
                return redirect(login_user)
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username != "" and password != "":
            query = authenticate(request, username=username, password=password)
            if query is None:
                messages.error(request, "Invalid Credentials")
            else:
                login(request, query)
                messages.success(request, 'Welcome To BugBounty')
                if UserProfile.objects.filter(user=request.user).exists():
                    return redirect(index)
                else:
                    return redirect(addUserProfile)
        else:
            messages.warning(request, "Null Values are not allowed")
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect(login_user)


@login_required(login_url='/login')
def user_profile(request):
    query = UserProfile.objects.filter(user=request.user)
    if query:
        return render(request, 'profile.html', {"query": query})
    else:
        return redirect(addUserProfile)


def addUserProfile(request):
    if request.method == "POST":
        UserProfile.objects.create(user=request.user, profilepicture=request.FILES.get('profile'), username=request.user, banner=request.FILES.get(
            'banner'), about=request.POST['about'], phone=request.POST['phone'], bugcrowd=request.POST['bugcrowd'], fb=request.POST['facebook'], twitter=request.POST['twitter'], insta=request.POST['instagram'])
        messages.info(request, "Data Updated Sccessfully")
        return redirect(user_profile)
    return render(request, 'addprofile.html')


@login_required(login_url='/login')
def updateUserProfile(request):
    query = UserProfile.objects.filter(user=request.user).first()
    context = UserProfile.objects.filter(user=request.user)
    if request.method == "POST":
        profile_picture = request.FILES.get('profile')
        banner_picture = request.FILES.get('banner')
        about = request.POST.get('about')
        phone = request.POST.get('phone')
        bugcrowd = request.POST.get('bugcrowd')
        fb = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        insta = request.POST.get('instagram')

        if profile_picture:
            query.profilepicture = profile_picture
        if banner_picture:
            query.banner = banner_picture

        query.about = about
        query.phone = phone
        query.bugcrowd = bugcrowd
        query.fb = fb
        query.twitter = twitter
        query.insta = insta

        query.save()

        messages.info(request, "Data Updated Successfully")
        return redirect(user_profile)

    return render(request, 'addprofile.html', {"query": context})


@login_required(login_url='/login')
def createPost(request):
    try:
        if request.method == "POST":
            Posts.objects.create(
                user=request.user, title=request.POST['title'], description=request.POST['describtion'], tags=request.POST['tags'])
            messages.info(request, "Post Created Successfully")
            return redirect(viewPosts)
        return render(request, 'createpost.html')
    except Exception as e:
        print(e)


@login_required(login_url='/login')
def sentCollabarationMessage(request, id):
    if request.method == "POST":
        post_instance = get_object_or_404(
            Posts, pk=id)  # Retrieve the Posts instance
        collaborate.objects.create(
            user=request.user, post=post_instance, description=request.POST['message'])  # Assign post_instance to the post field
        messages.info(request, 'Message sent successfully')
        return redirect('index')


@login_required(login_url='/login')
def viewCollabs(request):
    list = []
    instance = Posts.objects.filter(user=request.user)
    for val in instance:
        find = collaborate.objects.filter(post=val.id)
        if find:
            list.extend(find)
    return render(request, 'viewcollabrequests.html', {"list": list})


def viewPublicProfile(request, username):
    query = UserProfile.objects.filter(username=username)
    return render(request, 'publicprofile.html', {"query": query})


@login_required(login_url='/login')
def viewPosts(request):
    query = Posts.objects.filter(user=request.user)
    return render(request, 'viewposts.html', {"query": query})


@login_required(login_url='/login')
def deletePost(request, id):
    query = Posts.objects.get(id=id)
    if query.user == request.user:
        query.delete()
        messages.info(request, 'Post Deleted')
        return redirect(viewPosts)
    return redirect(viewPosts)


@login_required(login_url='/login')
def updatePost(request, id):
    query = Posts.objects.get(id=id)
    if request.method == "POST" and query.user == request.user:
        query.title = request.POST['title']
        query.description = request.POST['describtion']
        query.tags = request.POST['tags']
        query.save()
        messages.info(request, 'Post updated Successfully')
        return redirect(viewPosts)
    return render(request, 'editposts.html', {"query": query})
