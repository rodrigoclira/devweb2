# Autenticação usando OAUTH2 com o Python Social Auth

Este projeto tem como objetivo destacar a utilização do oauth2 com Django. Neste exemplo será possível se autenticar no sistema utilizando uma conta do Google, além das autenticações por e-mail e a padrão do Django.


## Pré-requisitos
| Instalar dependências informadas no arquivo 'requirements.txt' 

## Comandos

Vários serviços de redes sociais não permitem utilizar o localhost como destino de redirecionamento, por isso iremos criar um domínio interno na máquina. Com uma configuração local, iremos informar ao computador que um determinado domínio está no nosso localhost. Para fazer isso no Linux ou MacOs, edite o arquivo */etc/hosts* e adicione: 

```
127.0.0.1 mysite.com
```
No windows o arquivo a ser modificado é *C:\Windows\System32\Drivers\etc\hosts*. A partir de agora 'mysite.com' é um alias para o localhost. 
Para que essa mudança seja aceita no django, edite a variável ALLOWED_HOSTS do *settings.py* para conter o 'mysite.com'. 

```
ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']
```


Para executar projeto django utilize os comandos abaixo na pasta principal do projeto. 

Se for a primeira vez que esteja executando 
```
$ python manage.py makemigrations
```

e em seguida inicie a aplicação usando o seguinte comando:
```
python manage.py runserver_plus --cert-file cert.crt
```


Por fim, acesse a página inicial no navegador: 

[https://mysite.com:8000/projeto/](https://mysite.com:8000/projeto/)

> note que agora estamos usando https para que a autenticação usando oauth2 funcine. 

Agora você pode optar por logar com a sua conta do Google. 

![image](https://user-images.githubusercontent.com/276077/143514219-3e5ae815-edfb-4ca4-8a33-9a8e4ea0e5bc.png)

## Informações sobre a autenticação Oauth2. 

O [python social auth possui](https://github.com/python-social-auth/social-app-django) uma backend de autenticação para django. A instalação desse backend facilita a inclusão de autenticações usando redes sociais ([ver lista completa](https://python-social-auth.readthedocs.io/en/latest/intro.html#features)). Os passos listados abaixo já foram realizados para o projeto atual, mas podem ser reutilzidos para criação de novos projetos: 

1. É necessário instalar o pacote para django

```
pip install social-auth-app-django
``` 

2. em seguida adicionar o 'social_django' como um novo app do projeto na variável INSTALLED_APPS do settings.py. 

```
INSTALLED_APPS = [
...
'social_django',
}
```

3. A adição do novo app requer que sejam feitas as migrações necessárias
```
python manage.py migrate
```

4. Agora é necessário adicionar as urls da autenticação social. Elas seguem um padrão que deve ser replicado. No seu urls.py principal, adicione o seguinte path: 

```
path('social-auth/', include("social_django.urls"), name='social')
```

5. O redicionamento das redes sociais não funcionam para localhost ou 127.0.0.1, por isso você precisa criar um domínio interno na sua máquina, como apresentado  [AQUI](#Comandos)
