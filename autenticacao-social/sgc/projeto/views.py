from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import ColaboradorProjeto, Projeto, ProjetoTag, Tag, Comentario
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def listar(request, tag_name = ""):

    if tag_name:
        print(tag_name)
        projetosTags = ProjetoTag.objects.filter(tag__tag = tag_name)
        projetos = [projetoTag.projeto for projetoTag in projetosTags]
    else:
        projetos = Projeto.objects.all()

    context = {'projetos': projetos}
    return render(request, 'projeto/list.html', context)

@login_required
def exibir(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk = projeto_id) 
    coolaboradores = ColaboradorProjeto.objects.filter(projeto=projeto)
    tags = ProjetoTag.objects.filter(projeto=projeto)

    if settings.COMMENTS:
        comentarios = Comentario.objects(projeto = projeto_id)
    else:
        comentarios = []

    context = {
        'projeto': projeto,
        'colaboradores': coolaboradores,
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
