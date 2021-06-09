from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import ColaboradorProjeto, Projeto, ProjetoTag, Tag, Comentario


# Create your views here.
def listar(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'projeto/list.html', context)

def exibir(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk = projeto_id) 
    coolaboradores = ColaboradorProjeto.objects.filter(projeto=projeto)
    tags = ProjetoTag.objects.filter(projeto=projeto)
    comentarios = Comentario.objects(projeto = projeto_id)
    print(comentarios)
    context = {
        'projeto': projeto,
        'colaboradores': coolaboradores,
        'tags': tags,
        'comentarios': comentarios,
    }

    return render(request, 'projeto/detail.html', context)

def comentar(request):
    if request.is_ajax():
        texto = request.GET.get('comentario')
        projeto = request.GET.get('projeto')
        comentario = Comentario(projeto=projeto, texto=texto)
        comentario.save()
        return JsonResponse({'texto': texto, 'projeto': projeto, 'status':'ok'}, status=200)
    
