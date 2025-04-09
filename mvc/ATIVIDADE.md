# Atividade: Criando um Novo Aplicativo "Eventos"

> Tutorial desenvolvido por [Eduardo](https://github.com/Eduardo-J-S) como atividade da monitoria do semestre de 2024.2

Este tutorial mostra, passo a passo, como criar um novo aplicativo no Django para gerenciar eventos associados a projetos. Vamos desenvolver o aplicativo "eventos", entender as alterações no código e aprender boas práticas de organização em projetos Django.

## 1. Criar o Aplicativo
Primeiro, criamos o aplicativo (app) com o comando:
```cmd
python manage.py startapp eventos
```
### Por que criar um aplicativo separado?
Criar aplicativos distintos ajuda a manter o código organizado. Assim, "eventos" ficará responsável apenas pela lógica de gerenciamento de eventos, enquanto o aplicativo "projeto" cuidará dos projetos institucionais.

## 2. Configurar o Aplicativo no Projeto Django
Após criar o aplicativo, precisamos informá-lo ao Django. Para isso, adicionamos o aplicativo `eventos` em `INSTALLED_APPS` no arquivo `settings.py`:

```python
INSTALLED_APPS = [
    # outros apps
    'eventos',
]
```
Essa configuração garante que o Django reconheça o aplicativo e o inclua no ciclo de carregamento.

## 3. Criar o Modelo `Evento`
No arquivo `eventos/models.py`, definimos o modelo `Evento`. Ele representa os eventos no banco de dados, contendo informações como título, descrição, data e a relação com um projeto.

```python
from projeto.models import Projeto

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data = models.DateTimeField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="eventos")

    def __str__(self):
        return f"{self.titulo} - {self.projeto.titulo}"
```
### Entendendo o código
- `titulo`: Nome do evento.
- `descricao`: Detalhes opcionais sobre o evento.
- `data`: Quando o evento ocorrerá.
- `projeto`: Relaciona o evento a um projeto, permitindo buscar eventos de um projeto específico.

### Atualizar o banco de dados:
Após criar o modelo, aplicamos as migrações para refletir a mudança no banco de dados:
```
python manage.py makemigrations eventos
python manage.py migrate
```

## 4. Criar as Views
As views controlam o que acontece quando o usuário acessa uma página ou realiza uma ação no aplicativo.

**Listar Eventos:**
Criamos a view `listar_eventos` para exibir todos os eventos relacionados a um projeto específico:
```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from projeto.models import Projeto

def listar_eventos(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    eventos = projeto.eventos.all()
    context = {'projeto': projeto, 'eventos': eventos}
    return render(request, 'eventos/list.html', context)
```

**Criar Evento:**
A view `criar_evento` processa o formulário para adicionar novos eventos:
```python
from django.http import HttpResponse

def criar_evento(request):
    if request.method == 'POST':
        projeto_id = request.POST.get('projeto_id') 
        projeto = get_object_or_404(Projeto, id=projeto_id)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        if titulo and data:
            Evento.objects.create(
                titulo=titulo,
                descricao=descricao,
                data=data,
                projeto=projeto
            )
            return redirect('listar_eventos', projeto_id=projeto.id)

    projetos = Projeto.objects.all()
    return render(request, 'eventos/form.html', {'projetos': projetos})
```

## 5. Configuração de URLs
Adicionamos as rotas no arquivo `eventos/urls.py`:

```python
from django.urls import path

from . import views 

urlpatterns = [
    path('<int:projeto_id>/', views.listar_eventos, name='listar_eventos'),
    path('novo/', views.criar_evento, name='criar_evento'),
]
```
`<int:projeto_id>/`: Exibe uma lista com todos os eventos associados a um projeto específico. 
`novo/`: Permite que o usuário crie um novo evento para um projeto específico.

**E no arquivo `sgc/urls.py` principal, incluímos as rotas do aplicativo:**

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projeto/', include('projeto.urls')),  
    path('eventos/', include('eventos.urls')), 
]
```

## 4. Criar os Templates

**Template para Listar Eventos**
O template `eventos/list.html` exibe os eventos de um projeto:

```html
{% extends 'base.html' %}
{% block title %}Eventos de {{ projeto.titulo }}{% endblock %}
{% block content %}
<h1>Eventos de "{{ projeto.titulo }}"</h1>
<ul>
    {% for evento in eventos %}
        <li>
            <strong>{{ evento.titulo }}</strong>: {{ evento.data|date:"d/m/Y H:i" }}
            <p>{{ evento.descricao }}</p>
        </li>
    {% endfor %}
</ul>
<a href="{% url 'criar_evento' %}" class="btn btn-primary">Adicionar Evento</a>
<a href="{% url 'listar' %}">Voltar para Projetos</a>
{% endblock %}
```

**Template para Criar Evento**
O formulário `eventos/form.html` permite adicionar novos eventos:

```html
{% extends 'base.html' %}
{% block title %}Criar Evento{% endblock %}
{% block content %}
<div class="py-3 text-left">
    <h1>Criar Evento</h1>
</div>
<div class="row">
    <div class="col-md-8">
        <form method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="projeto_id">Projeto:</label>
                <select name="projeto_id" id="projeto_id" class="form-select" required>
                    {% for projeto in projetos %}
                        <option value="{{ projeto.id }}">{{ projeto.titulo }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="form-group">
                <label for="titulo">Título:</label>
                <input type="text" name="titulo" id="titulo" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="descricao">Descrição:</label>
                <textarea name="descricao" id="descricao" class="form-control"></textarea>
            </div>
            <div class="form-group">
                <label for="data">Data:</label>
                <input type="datetime-local" name="data" id="data" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Salvar</button>
            <a href="{% url 'listar' %}" class="btn btn-secondary">Cancelar</a>
        </form>
    </div>
</div>

<style>
    .form-group {
        margin-bottom: 1rem;
    }
</style>
{% endblock %}
```

## 7. Registrar o Modelo no Admin
Para facilitar a gestão de eventos durante o desenvolvimento, registramos o modelo no painel administrativo `eventos/admin.py`:

```python
from django.contrib import admin
from .models import Evento

admin.site.register(Evento)
```

Ao registrar o modelo `Evento`, podemos criar, editar e excluir eventos diretamente no painel administrativo, o que é útil durante o desenvolvimento.

## 8. Testar e Melhorar
- Execute o servidor local:
```cmd
pip install -r requirements.txt
```

Acesse as rotas para testar a funcionalidade.O servidor será iniciado no endereço http://127.0.0.1:8000/:
- http://127.0.0.1:8000/eventos/<projeto_id>/: Lista os eventos de um projeto. 
- http://127.0.0.1:8000/eventos/novo/: Adiciona um novo evento.

**Desafios Extras**
1. Adicionar páginas para editar e excluir eventos.
2. Melhorar os templates com estilos CSS.

