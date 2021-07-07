"""sgc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projeto/', include('projeto.urls')),
    #path('login/', auth_views.LoginView.as_view(), name="login"),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    #path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password-change-done'),
    path('', include('core.urls')),
    path('', include("django.contrib.auth.urls")),
    path('social-auth/', include("social_django.urls"), name='social'),
]
