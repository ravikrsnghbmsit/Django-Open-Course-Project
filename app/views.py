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

def home(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user = user)
    context = {
        "user":user,
        "user_info":user_info,
    }
    return render(request , 'home.html', context)
