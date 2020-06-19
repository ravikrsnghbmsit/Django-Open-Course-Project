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
