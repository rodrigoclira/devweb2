# Mapeamento (Roteamento) URL

Este projeto tem como objetivo destacar a utilização das diferentes formas de realizar mapeamento de URL. Todos os exemplos estão apresentados nos arquivos 'urls.py' do projeto.


## Pré-requisitos

> 1. **Instalar bibliotecas** informadas no arquivo 'requirements.txt' 

```bash
pip3 install -r requirements.txt
```

> 2. **Instalação do MongoDB**
> 
> Use o tutorial do site do MongoDB que seja compatível com o seu SO. 
> Link direto para o [Amazon Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/).
> Após a instalação, confirme se o daemon foi iniciado. Caso contrário, inicie-o. 

## Base de Dados
Este exemplo usa o banco de dados mongodb e sqlite. Qualquer mudança referente a isso pode ser realizada no arquivo *sgc/settings.py* . Lá você pode 
desabilitar a utilização do mongodb ao modificar a variável *COMMENTS* para False. Alterações para utilização de outro banco de dados
relacional devem ser feitas na variável *DATABASES* que atualmente já suporta o sqlite quando *PROD_ENV=False* ou Postgres, quando o *PROD_ENV=True*.

> Como usar o banco de dados de exemplo? (Carregar o dump)
> ```
> python manage.py loaddata sql/dump-db.yaml
> ```
> Se não utilizar o dump de banco de exemplo, será necessário acessar o painel de 
> administração do django e criar entradas para as entidades.

## Para executar projeto django utilize os comandos abaixo na pasta principal do projeto. 

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


## Mepeamento de URL usando outras frameworks

- [Spring boot (Request Mapping)](https://www.baeldung.com/spring-requestmapping)

- [Node (Express)](https://expressjs.com/pt-br/guide/routing.html)

- [Django (urls)](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

## Material Complementar

https://cs.lmu.edu/~ray/notes/regex/

https://regexr.com/
