from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    path('calc', views.calc, name='calc'),
]
