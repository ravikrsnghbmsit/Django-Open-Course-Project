from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        image = request.FILES['image']
        user = User.objects.create(username = email , first_name = first_name ,last_name = last_name , email=email)
        print("User object is created")
        user.password = make_password(password)
        user.save()
        print("Password Changed Successfully")
        userinfo.objects.create(user = user , Birthday = birthday , Gender = gender , profile_pic = image)
        print("UserInfo is Added")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request,'signup.html',)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username ,password=password)
        if user:
            login(request,user)
            print("User has logged in")
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
        else:
            print("Wrong password")
            return HttpResponse("Somebody Tried to login but he failed")
    return render(request,'signup.html',)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:signup'))

def home(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user = user)
    all_posts = Post.objects.all().order_by('-pk')
    all_users = userinfo.objects.all()
    context = {
        "user":user,
        "user_info":user_info,
        "all_posts":all_posts,
        "all_users":all_users,
    }
    return render(request , 'home.html', context)


def makepost(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user = user)
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            post_img = request.FILES['image']
        except:
            post_img = None
        try:
            post_video = request.FILES['video']
        except:
            post_video=None
        Post.objects.create(user=user , user_info = user_info , text = text , image = post_img , video = post_video , l =0 , c=0)
        print("Post Created Successfully")
        return HttpResponseRedirect(reverse('app:home' , args=(user.id,)))

def likepost(request):
    print("Hey I am working")
    post_id = request.GET.get('post_id')
    user_id = request.GET.get('user_id')
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=user_id)
    if likes.objects.filter(post = post).filter(user = user).exists():
        post.l = post.l - 1;
        post.save()
        likes.objects.filter(post=post).filter(user = user).delete()
        return HttpResponse(post.l)
    post.l = post.l + 1
    likes.objects.create(user = user , post =post)
    post.save()
    return HttpResponse(post.l)
