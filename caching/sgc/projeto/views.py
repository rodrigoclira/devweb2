from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import ColaboradorProjeto, Projeto, ProjetoTag, Tag, Comentario
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.
def listar(request, tag_name = ""):

    if tag_name:
        print(tag_name)
        key = f"{tag_name}_projetos"
        projetos =  cache.get(key)
        if not projetos:
            projetosTags = ProjetoTag.objects.filter(tag__tag = tag_name)
            projetos = [projetoTag.projeto for projetoTag in projetosTags]
            cache.set(key, projetos, 45)
        else:
            print ("usou o cache")
    else:
        projetos = cache.get("all_projetos")
        if not projetos:            
            projetos = Projeto.objects.all()
            cache.set("all_projetos", projetos, 45)
        else:
            print ("usou o cache")

    context = {'projetos': projetos}
    return render(request, 'projeto/list.html', context)

@login_required
def exibir(request, projeto_id):
    
    key_proj =  f"{projeto_id}_projeto"
    projeto = cache.get(key_proj)
    if not projeto:
        projeto = get_object_or_404(Projeto, pk = projeto_id) #consultando no banco sqlite
        cache.set(key_proj, projeto, 45)
    else:
        print ("usou o cache")

    key_colab = f'{projeto_id}_colab'
    colaboradores = cache.get(key_colab)
    if not colaboradores:
        colaboradores = ColaboradorProjeto.objects.filter(projeto=projeto)
        cache.set(key_colab, colaboradores, 45)
    else:
        print ("usou o cache")

    key_tags = f"{projeto_id}_tags"
    tags = cache.get(key_tags)
    if not tags:       
        tags = ProjetoTag.objects.filter(projeto=projeto)
        cache.set(key_tags, tags, 45)      
    else:
        print ("usou o cache")

    if settings.COMMENTS:
        key_comment = f'{projeto_id}_comentario'
        comentarios = cache.get(key_comment)
        if not comentarios:
            comentarios = Comentario.objects(projeto = projeto_id)
            cache.set(key_comment, comentarios, 45)
        else:
            print ("usou o cache")
    else:
        comentarios = []

    context = {
        'projeto': projeto,
        'colaboradores': colaboradores,
        'tags': tags,
        'comentarios': comentarios,
        'comentario_settings': settings.COMMENTS
    }

    return render(request, 'projeto/detail.html', context)

def comentar(request):
    if request.is_ajax():
        texto = request.GET.get('comentario')
        projeto = request.GET.get('projeto')
        comentario = Comentario(projeto=projeto, texto=texto)
        comentario.save()
        return JsonResponse({'texto': texto, 'projeto': projeto, 'status':'ok'}, status=200)
    
def listar_tag(request, tag_id):
    pass
