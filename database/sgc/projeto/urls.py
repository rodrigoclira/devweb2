from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.listar, name='listar'), #projeto/
    path('exibir/<int:projeto_id>', views.exibir, name='exibir'), #projeto/exibir/2
    path('comentar/', views.comentar, name='comentar'),
]
