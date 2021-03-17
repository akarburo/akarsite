from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = "user"

urlpatterns = [

    path('register/', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    url(r'^account/$', views.change_password, name='change_password'),
]