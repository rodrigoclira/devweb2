from django.urls import path
from django.views.decorators.cache import cache_page
from . import views 

#https://docs.djangoproject.com/en/3.2/topics/http/urls/
app_name = 'projeto'
urlpatterns = [ 
    path('', views.listar, name='listar'), #projeto/
    path('<int:projeto_id>', views.exibir, name='exibir'), #projeto/exibir/2
    path('tag/<str:tag_name>', cache_page(60)(views.listar), name='listar_tag'), #projeto/exibir/tag/iot
    path('comentar/', views.comentar, name='comentar'),
]

