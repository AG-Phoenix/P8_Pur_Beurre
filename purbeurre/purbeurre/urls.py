"""purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from listing import views as lviews
from accounts import views as aviews

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', lviews.index, name='index'),
    path('register/', aviews.register_page, name='register'),
    path('login/', aviews.login_page, name='login'),
    path('logout/', aviews.logout_user, name='logout'),
    path('profile/', aviews.profile_page, name='profile'),
    path('saved/', lviews.saved, name='saved'),
    path('legals/', lviews.legals, name='legals'),
]
