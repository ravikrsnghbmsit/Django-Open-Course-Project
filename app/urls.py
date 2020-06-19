from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('',views.signup,),
    path('user_login/',views.user_login,name="login"),
    path('home/<int:pk>/',views.home,name="home"),
    path('makepost/<int:pk>/',views.makepost,name="makepost"),
]
