
from django.urls import path

from . import views 

#https://docs.djangoproject.com/en/3.2/topics/http/urls/
app_name = 'core'

urlpatterns = [ 
    path('registrar/', views.registrar, name='registrar'),
]


