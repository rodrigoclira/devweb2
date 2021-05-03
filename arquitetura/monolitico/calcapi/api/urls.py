from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    path('calc', views.calc, name='calc'),
    path('soma', views.soma, name='soma'),
    path('sub', views.sub, name='sub'),
]
