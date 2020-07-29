"""Main_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from Student.views import *
from Teacher.views import *
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from CoreApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login',CustomTokenObtainPairView.as_view()),
    path('api/refresh_token',TokenRefreshView.as_view()),
    path('api/student/',include('Student.urls')),
    path('api/teacher/',include('Teacher.urls')),
    path('api/homepage/',include('HomePage.urls')),
    path('api/school/',include('School_Details.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
