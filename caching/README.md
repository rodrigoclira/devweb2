# Exemplo de projeto com a API de Cache do Djnago


Este projeto tem como objetivo destacar a utilização da api de cache do django e o memcached. 
<br>
Neste projeto o memcached é utilizado como banco de cache das informações do banco.


## Pré-requisitos

> 1. **Instalar bibliotecas** informadas no arquivo 'requirements.txt' 
>
> ```bash
> pip3 install -r requirements.txt
> ```

> 2. **Inicializar o Memcached**
> 
> Você pode usar o tutorial do site do Memcached para instalar o banco. 
> https://memcached.org/downloads
> 
> Após a instalação, inicie-o com o seguinte comando:
> 
> ```memcached -l 127.0.0.1:11211```

> 3. **Usar o Memcached no container**
> 
> Ou inicializar o memcached no container que está na pasta 'docker' do projeto. 
> para inicializar, execute ```sudo docker-compose up --build -d``` e para 
> desligar, use o ```sudo docker-compose down``` na mesma pasta.



## Comandos

Para executar projeto django utilize os comandos abaixo na pasta principal do projeto.

Se for a primeira vez que esteja executando 
```
$ python manage.py makemigrations
```

e em seguida inicie a aplicação:
```
$ python manage.py runserver_plus --cert-file cert.crt
```

Por fim, acesse a página inicial no navegador: 

https://127.0.0.1:8000/projeto/

## Caching em Django

Através da framework de cache do django é possível criar cache de baixo nível, requisição e template.

### Exemplo de cache de fragmentos de template 

Arquivo de exemplo: sgc/templates/projeto/detail.html
```html
{% load cache %} 

{% cache 60 content module %}

	<div class="col-md-5 order-md-2">
			<h4 class="mb-3 text-center">Descrição</h4>
				{% csrf_token %}
			<div class="form-row ">
				<div class="form-group">
					<p class="text-justify">{{ projeto.descricao }}</p>
				</div>
			</div>

			<div class="form-group col-md-11">
					<label for="inputTipo">Tags</label>
					<div class="form-group">
						{% for tag in tags %}
							<a href="{% url 'projeto:listar_tag' tag.tag %}" target="_blank" >{{ tag.tag|upper }}</a>
						{% endfor %}
					</div>

			</div>
	</div>
	
	<!-- Left column -->
	<div class="col-md-7 order-md-1">
		<h4 class="mb-3">{{projeto.titulo}}</h4>
        <hr class="my-4">

	 	<input type="hidden" id="projetoId" value="{{projeto.pk}}">

        <div class="form-row">
			<div class="form-group col-md-11">
				<label for="div-coordenador">Nome do Coordenador</label>
                <div id="div-coordenador form-control">{{projeto.coordenador.nome}}</div>
			</div>				
		</div>

        <hr class="my-4">

		<div class="form-row">
			<div class="form-group col-md-11">
				<label for="div-email">E-mail</label>
                <div id="div-email form-control">{{projeto.coordenador.email}}</div>
			</div>
        </div>				

        <hr class="my-4">

        <div class="form-row">

			<div class="form-group col-md-11">
				<label for="div-lattes">Lattes</label>
                <div id="div-lattes form-control">
                    <a href="{{projeto.coordenador.lattes}}" target="_blank">{{projeto.coordenador.lattes}}</a>
                </div>
            </div>				
		</div>
        
        <hr class="my-4">

		<div class="form-row">
			<div class="form-group col-md-11">
					<label for="inputTipo">Colaboradores</label>
                    <ul class="list-group list-group-flush">

                    {% for colaborador in colaboradores %}
                        <li class="list-group-item"><a href="#" target="_blank" >{{colaborador.colaborador.nome}}</a></li>
                    {% endfor %}
                    </ul>
			</div>
		</div>

        <hr class="my-4">


		<h4/>	

		{% if comentario_settings %}
			{% include "projeto/comentario.html"  with comentarios=comentarios%}
		{% endif %}

		{% endcache %}
```

### Exemplo de cache de requisição

Arquivo de exemplo: sgc/projeto/urls.py

```python
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
```

### Exemplo de cache de baixo nível

Arquivo de exemplo: sgc/projeto/views.py

```python
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
```

### Teste de carga usando o JMeter 

[How to Use JMeter for Performance & Load Testing](https://www.guru99.com/jmeter-performance-testing.html)

