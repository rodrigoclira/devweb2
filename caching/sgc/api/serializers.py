from django.contrib.auth import authenticate
from rest_framework import serializers
from projeto.models import Projeto, TipoProjeto, Tag, ProjetoTag, ColaboradorProjeto, Tipo
from core.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'email']

class ProjetoSerializerList(serializers.ModelSerializer): # Corrigir
    class Meta:
        model = Projeto
        fields = ['titulo', 'pk']

class ProjetoSerializer(serializers.ModelSerializer):
    coordenador = ProfessorSerializer(many = False, read_only = True)

    class Meta:
        model = Projeto
        fields = ['pk', 'titulo', 'descricao', 'inicio', 'fim', 'aprovado', 'coordenador']

class ColaboradorProjetoSerializer(serializers.ModelSerializer):
    projeto = ProjetoSerializer(many = False, read_only = True)
    colaborador = ProfessorSerializer(many = False, read_only = True)
    class Meta:
        model = ColaboradorProjeto 
        fields = ['projeto', 'coolaborador']   


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

class ProjetoTag(serializers.ModelSerializer):
    projeto = ProjetoSerializer(many = False, read_only = True)
    tag = TagSerializer(many = True, read_only = True)
    class Meta:
        model = ProjetoTag
        fields = ['projeto', 'tag']


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['nome']

class TipoProjetoTipoSerializer(serializers.ModelSerializer):
    projeto = ProjetoSerializer(many = False, read_only = True)
    tipo = TipoSerializer(many = False, read_only = True)
    class Meta:
        model = TipoProjeto
        fieds = ['projeto', 'tipo']