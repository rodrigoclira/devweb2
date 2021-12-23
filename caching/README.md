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

> 2. **Instalação do Memcached**
> 
> Use o tutorial do site do Memcached para instalar o banco. 
> https://memcached.org/downloads
> 
> Após a instalação, inicie-o com o seguinte comando:
> 
> ```memcached -l 127.0.0.1:11211```


## Comandos

Para executar projeto django utilize os comandos abaixo na pasta principal do projeto.

Se for a primeira vez que esteja executando 
```
$ python manage.py makemigrations
```

e em seguida inicie a aplicação:
```
$ python manage.py runserver
```

Por fim, acesse a página inicial no navegador: 

http://127.0.0.1:8000/projeto/
