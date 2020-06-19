from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('',views.signup,name="signup"),
    path('user_login/',views.user_login,name="login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('home/<int:pk>/',views.home,name="home"),
    path('makepost/<int:pk>/',views.makepost,name="makepost"),
    path('likepost/',views.likepost,name="likepost"),
]
