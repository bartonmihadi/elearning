"""letty URL Configuration

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
from school import views as school_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',include('school.urls')),
    path('admin/', admin.site.urls),
    path('register/',school_view.register,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='Login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',school_view.profile,name='profile'),
]
