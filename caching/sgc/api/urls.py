from typing import ValuesView
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
     path("projetos/", views.ProjetoListView.as_view(), name="api_projeto_list"),
     path("projetos/<pk>", views.ProjetoDetailView.as_view(), name="api_projeto_detail"),
]
