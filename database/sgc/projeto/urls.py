from django.urls import path

from . import views 

#https://docs.djangoproject.com/en/3.2/topics/http/urls/
app_name = 'projeto'
urlpatterns = [ 
    path('', views.listar, name='listar'), #projeto/
    path('<int:projeto_id>', views.exibir, name='exibir'), #projeto/2
    path('tag/<str:tag_name>', views.listar, name='listar_tag'), #projeto/tag/iot
    path('comentar/', views.comentar, name='comentar'),
]

