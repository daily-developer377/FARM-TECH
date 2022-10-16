"""farmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from farmapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.index),

    path('contact',views.contact),
    path('common',views.common),
    path('login',views.login),
    path('registration',views.registration),
    path('UserHome',views.UserHome),

    path('farmerprofile',views.farmerprofile),
    path('acceptloan',views.acceptloan),
    path('Addcropdetails',views.Addcropdetails1),
    path('farmerviewcrop',views.farmerviewcrop),
   
    path('Adminviewcrop',views.Adminviewcrop),
    path('Adminviewfarmer',views.Adminviewfarmer),

    path('AdminaddNews',views.AdminaddNews),
    path('Farmerviewnews',views.Farmerviewnews),

     path('Adminaddloantype',views.Adminaddloantype),
    path('deleteloan',views.deleteloan),

    path('farmerviewloan',views.farmerviewloan),
    path('farmerrequestloan',views.farmerrequestloan),
    path('farmerviewloanstatus',views.farmerviewloanstatus),
    path('collectcrop',views.collectcrop),
    path('adminviewcropcollection',views.adminviewcropcollection),
    path('adminadddelivaryboy',views.adminadddelivaryboy),
    path('adminviewloan',views.adminviewloan),
     path('delivaryviewcrop',views.delivaryviewcrop),
    path('payment1',views.payment1),
    path('payment2',views.payment2),
    path('payment3',views.payment3),
    path('payment4',views.payment4),
    path('payment5',views.payment5),
      path('Addfeedback',views.Addfeedback),
        path('Viewfeedback',views.Viewfeedback),


]
