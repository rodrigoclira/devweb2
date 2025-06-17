from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('otp/setup/', views.otp_setup, name='otp_setup'),
    path('otp/verify/', views.otp_verify, name='otp_verify'),
    path('otp/disable/', views.disable_otp, name='disable_otp'),
    path('secure/', views.secure_view, name='secure_view'),
]

