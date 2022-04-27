# Autenticação usando OAUTH2 com o Python Social Auth

Este projeto tem como objetivo destacar a utilização do oauth2 com Django. Neste exemplo será possível se autenticar no sistema utilizando uma conta do Google, além das autenticações por e-mail e a padrão do Django.


## Pré-requisitos
| Instalar dependências informadas no arquivo 'requirements.txt' 

## Configuração

Vários serviços de redes sociais não permitem utilizar o localhost como destino de redirecionamento, por isso iremos criar um domínio interno na máquina. Com uma configuração local, iremos informar ao computador que um determinado domínio está no nosso localhost. Para fazer isso no Linux ou MacOs, edite o arquivo */etc/hosts* e adicione: 

```
127.0.0.1 mysite.com
```
No windows o arquivo a ser modificado é *C:\Windows\System32\Drivers\etc\hosts*. A partir de agora 'mysite.com' é um alias para o localhost. 

## Execução do Projeto

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

5. O redicionamento das redes sociais não funcionam para localhost ou 127.0.0.1, por isso você precisa criar um domínio interno na sua máquina, como apresentado  [AQUI](#Configuração). O 'mysite.com' foi o domínio usado para o teste local, mas se você estiver implantando a aplicação, lembre de atualizar para o domínio real.

6. Para que essa mudança seja aceita no django, edite a variável ALLOWED_HOSTS do *settings.py* para conter o 'mysite.com'. 

```
ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']
```

> A partir de agora vamos configurar o projeto para usar a autenticação com o email do google. Lembre-se que a biblioteca permite a autenticação com inúmeras redes sociais. 

7. Vamos adicionar o backend de autenticação do google na lista de backend disponíveis no projeto. O backend que deve ser adicionado é *social_core.backends.google.GoogleOAuth2* 

```
AUTHENTICATION_BACKENDS = [
    ...
    'social_core.backends.google.GoogleOAuth2'
]
```

9. Agora precisamos criar a aplicação no google para que possámos obter a chave de acesso a API, (*SOCIAL_AUTH_GOOGLE_OAUTH2_KEY*) e o (*SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET*) para configurar o módulo. 

10. Acesse o seu Google Developer Console [https://console.cloud.google.com/home/](https://console.cloud.google.com/home/). Na página crie um novo projeto, como indicado na imagem abaixo. 

![image](https://user-images.githubusercontent.com/276077/143516570-cb26d3e4-0d17-4a91-929d-5801c6ff9d9d.png)

11. Em seguida dê um nome ao seu projeto na plataforma do google e aperte em 'criar'. 

![image](https://user-images.githubusercontent.com/276077/143517017-9ead6ef3-93f3-4723-8b46-20bb36081d7c.png)


12. Com o projeto criado, clique em 'APIs e Serviços / Credenciais' 

![image](https://user-images.githubusercontent.com/276077/143517264-4d5d2b1e-29ca-4c32-88dc-c9a8e59e6fe3.png)

e selecione 'ID do Cliente Ouath'

![image](https://user-images.githubusercontent.com/276077/143517313-b2fd7101-c89c-4c71-b58b-c33841ac52e5.png)

13. Clique em 'Configura Tela de Consentimento'

![image](https://user-images.githubusercontent.com/276077/143517473-56358427-cbb4-4fb1-8713-25a246788dc6.png)

14. Escolha a opção 'Externo' para permitir que qualquer usuário com uma conta google acesso a aplicação. A opção 'Interno' é interessante quando você quer deixar a sua aplicação funcionando apenas para os usuários de uma determinada organização, como por exemplo *@paulista.ifpe.edu.br*. 

![image](https://user-images.githubusercontent.com/276077/143517602-d6f3f06c-e06f-401b-b33b-f3c2e2ba767f.png)

15. Configure o nome da aplicação, o email de contato e o domínio autorizado. Caso esteja rodando em ambiente local, lembre-se de criar um domínio interno.

![image](https://user-images.githubusercontent.com/276077/143517917-4de3c45e-3727-4e7f-97e7-dd173abb2171.png)
![image](https://user-images.githubusercontent.com/276077/143518367-a7187537-4934-41bb-b17c-2c21fe646321.png)


16. Prossiga clicando em 'Salvar e Continuar' até a tela de Resumo

![image](https://user-images.githubusercontent.com/276077/143518610-3972002d-1226-4558-903c-2412834395c0.png)


17. Por fim clique em 'Voltar para o Painel' na tela de Resumo. 

![image](https://user-images.githubusercontent.com/276077/143518761-aa0f8d01-927f-45cf-b257-a44d0d9eb621.png)

18. Novamente clique em 'Criar Credenciais' e Escolha 'ID do Cliente Oauth'

![image](https://user-images.githubusercontent.com/276077/143518927-b27c2412-cc7d-4e24-93cb-b4ad5ec19ffb.png)

19. Escolha 'Aplicação da Web'

![image](https://user-images.githubusercontent.com/276077/143518980-f65ad63d-4c71-4827-8602-e023e9cae0a0.png)

20. Agora é importante ter atenção para a URI de redirecionamento. Ela será usada para indicar a sua aplicação que a autenticação foi realizada com sucesso e segue um padrão definido pelo python social auth. A uri para o 'mysite.com' é 'https://mysite.com:8000/social-auth/complete/google-oauth2/' e o 'https://mysite.com:8000/social-auth/', como exibido na página abaixo. 

![image](https://user-images.githubusercontent.com/276077/143520584-698036ec-5b60-4d5a-a55d-364013fb782e.png)

21. Use as informações indicadas na tela abaixo para configurar as variáveis *SOCIAL_AUTH_GOOGLE_OAUTH2_KEY* e o *SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET* no settings.py

![image](https://user-images.githubusercontent.com/276077/143519479-310351cb-c2d4-4dae-87de-e61918ab8b21.png)


![image](https://user-images.githubusercontent.com/276077/143519561-af366817-ed82-42d1-aa6f-9b022559cba9.png)


22. Para finalizar a configuração na conta do google, ative o Google+ API seguindo os passos abaixo: 
![image](https://user-images.githubusercontent.com/276077/143519982-f70c9c20-7f2a-4dc1-9c0c-d2c8a770919d.png)


![image](https://user-images.githubusercontent.com/276077/143520050-92512198-bcee-4842-a6a3-f78ff00e22c5.png)

![image](https://user-images.githubusercontent.com/276077/143520084-3e9bc759-2bfa-4eed-a8b2-29b03c99736c.png)

23. Para adicionar o link do login social, escrevra o seguinte código html no seu template de login. 

```html
<li class="google">
        <a href="{% url "social:begin" "google-oauth2" %}">Login com o Google </a>
</li>
```



