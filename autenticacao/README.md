# Autenticação

Este projeto tem como objetivo discutir Autenticação utilizando o _framework_ Django.

# Usando o Framework Django

Django inclui um framework de autenticação pronto, com capacidade para lidar com
autenticações de usuários, sessões, permissões e grupos de usuários. O sistema de autenticação
inclui views para ações comuns do usuário, como logout, alteração de senha.

O framework de autenticação está em django.contrib.auth e é usado por outros pacotes do contrib
de Django. Ao criar um projeto Django com o comando *startproject*, o _fremework_ de autenticação
será incluído nas configurações *default* do projeto. Ele é composto da aplicação django.contrib.auth
e das duas classes de middleware a seguir:

  - _AuthenticationMiddleware_: associa os usuários às requisições usando sessões
  - _SessionMiddleware_: cuida da sessão atual durante as requisições

Middleware são classes com métodos uqe são executados globalmente durante a fase de requisição ou resposta.

A _framework_ de autenticação também inclui os modelos a seguir:
 - **User**: um modelo de usuário com campos básicos; os principais campos desse modelo são: _username_, _password_, _email_,
_first_name_, _last_name_ e _is_active_.
 - **Group**: um modelo de grupo para classificar os usuários.
 - **Permission**: _flags_ para usuários ou grupos poderem executar determinadas ações.

O _framework_ inclui também os _forms_ e _views_ padrões de autenticação.
A explicação do projeto está descrita em [Auth-Django.md](Auth-Django.md) e o passo a passo para execução no Cloud9 está em [AWS.md](AWS.md).

## Pré-requisitos
| Instalar dependências informadas no arquivo '_requirements.txt_' 

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



## Referências

[Autenticação de usuário no Django](https://docs.djangoproject.com/pt-br/3.2/topics/auth/)
