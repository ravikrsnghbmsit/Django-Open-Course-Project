from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Birthday = models.DateField(default = timezone.now)
    Gender = models.CharField(max_length = 10 , default="Male")
    about = models.CharField(max_length=200, blank = True)
    profile_pic = models.ImageField(upload_to='profile_pic/')
    cover_pic = models.ImageField(upload_to='cover_pic/')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_info = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    text = models.CharField(max_length=400,blank=True)
    image = models.ImageField(upload_to='post-images/',null=True)
    video = models.FileField(upload_to='post-videos/',null=True)
    l = models.IntegerField(default = 0)
    c= models.IntegerField(default = 0)

    def __str__(self):
        return self.user.first_name
