from rest_framework import generics 
from .serializers import ProjetoSerializer, ProjetoSerializerList
from projeto.models import Projeto
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ProjetoListView(generics.ListAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializerList

class ProjetoDetailView(generics.RetrieveAPIView):
    #authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)    
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer 