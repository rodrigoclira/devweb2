from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.listar, name='listar'),
    path('exibir/<int:projeto_id>', views.exibir, name='exibir'),
]
