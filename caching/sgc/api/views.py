from rest_framework import generics 
from .serializers import ProjetoSerializer, ProjetoSerializerList
from projeto.models import Projeto
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



class ProjetoListView(generics.ListAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializerList
    
    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProjetoDetailView(generics.RetrieveAPIView):
    #authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)    
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer 

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)