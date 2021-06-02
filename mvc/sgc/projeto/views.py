from django.shortcuts import render, get_object_or_404
from .models import ColaboradorProjeto, Projeto, ProjetoTag, Tag


# Create your views here.
def listar(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'projeto/list.html', context)

def exibir(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk = projeto_id) 
    coolaboradores = ColaboradorProjeto.objects.filter(projeto=projeto)
    tags = ProjetoTag.objects.filter(projeto=projeto)

    context = {
        'projeto': projeto,
        'colaboradores': coolaboradores,
        'tags': tags,
    }

    return render(request, 'projeto/detail.html', context)


