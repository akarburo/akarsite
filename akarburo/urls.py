"""akarburo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from akar import views
from django.conf.urls import url

app_name= "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name ="index"),
    path('about/', views.about,name ="about"),
    path('service/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('machines/',views.machines,name="machines"),
    path('consumables/',views.consumables,name="consumables"),
    path('user/',include("user.urls")),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('',views.home,name="home"),
    path('productdemand/',views.demand,name="demand"),
    path('success/',views.success,name="success"),
    path('test/',views.test,name="test"),
    path('products/',views.products,name="products"),
    path('logined/',views.logined,name="logined"),
    path('dboard/services/',views.dashservices,name="dashservices"),
    path('dboard/services/<int:id>',views.dashserviceupdate,name="dashserviceupdate"),
    path('dboard/pd/',views.dashpd,name="pd"),
    path('dboard/pd/<int:id>',views.dashpdupdate,name="dashpdupdate"),
    path('dboard/dashboardtest/',views.dashboardtest,name="dashboardtest"),
    path('dboard/account/',views.account,name="account"),

]
