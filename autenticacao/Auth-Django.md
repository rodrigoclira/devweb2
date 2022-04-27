# Autenticação no Django 

Neste documento serão apresentados todos as ações que permitiram utilizar a framework de autenticação do Django

## sgc/settings.py

No settings.py são adicionados as configurações do projeto. Por padrão o app que contém o sistema de autenticação do Django e os Middlewares necessários já são adicionados ao criar um novo projeto. 
![image](https://user-images.githubusercontent.com/276077/165422430-9fb04ff4-93f8-4d46-9596-8a8b32cfbf8b.png)


Na imagem abaixo estão destacadas duas informações, sendo elas a indicação das views de redirect quando ações da autenticação são realizadas como login e logout. Essas informações normalmente não são criadas automaticamente e depende do 'nome' atribuído no arquivo urls.py. 

A outra informação trata-se de um segundo backend de autenticação. Por padrão (**django.contrib.auth.backends.ModelBackend**) o Django vai validar as informações passadas no login levando em consideração o '_username_' e o '_password_', contudo o segundo backend (**core.authentication.EmailAuthBackend**) permite que o usuário faça login digitando o seu e-mail como 'username'. 

![image](https://user-images.githubusercontent.com/276077/165422510-d657f110-160e-46ca-8dac-de871a86cf88.png)

Caso você não queira a funcionalidade indicada de login usando também o e-mail, não precisa adicionar nenhum novo _backend_ de autenticação. 

## sgc/urls.py

O urls.py da pasta sgc é o principal arquivo de rotas do projeto. Ele normalmente incorpora outros arquivos de rotas, centralizando esse processo de rotamento. No arquivo atual já há as rotas do sistema de adminitração ('/admin') e do app projeto ('/projeto'). Para a adição das funcionalidades de autenticação precisam ser adicionados novas rotas. Nesse caso foram adicionados rotas sobrescritas - as contidas no _core.urls_ - e rotas já definidas pelo app de autenticação do django (django.contrib.auth.urls). 

O django.contrib.auth.urls já engloba diversas rotas do sistema, mas elas poderiam também ser listadas uma a uma (como no código comentado). 

![image](https://user-images.githubusercontent.com/276077/165423893-49cf9ad0-8822-46f8-ac83-aeac2af81202.png)

## core/urls.py
Foi decidido criar um próprio formulário de registro para o projeto. Ele pode ser acessado na rota /registrar .
![image](https://user-images.githubusercontent.com/276077/165424101-83f5c971-3019-4a5a-a828-3ef184c496e5.png)

## core/views.py

A view que realiza o registro de um novo usuário utiliza o form 'UserRegistrationForm'. 
![image](https://user-images.githubusercontent.com/276077/165424490-57beccc3-0438-45a9-9cfd-fed314f4ba79.png)

## core/forms.py

![image](https://user-images.githubusercontent.com/276077/165424761-a8d7c153-f6ac-4771-a8d8-c3505f9cf937.png)

## core/Autentication.py
Abaixo há o conteúdo do arquivo 'EmailAuthBackend' que está é indicado no settings.py
![image](https://user-images.githubusercontent.com/276077/165423133-b2022b4a-83a3-4300-8b62-064434e47ff0.png)

## templates
Na pasta template são adicionados os templates das páginas de autenticação. A de registro foi criada como sendo uma funcionalidade do app 'core', logo ela fica disponível na pasta 'templates/core', todas as outras que pertecem a 'django.contrib.auth' devem ficar na pasta 'templates/registration'
Sendo assim esses são os templates adicionados

### templates/core/registration_realizado.html
![image](https://user-images.githubusercontent.com/276077/165425353-c443e1b7-47f7-42ad-a0b1-9e998751f6b6.png)


## templates/core/registro.html
![image](https://user-images.githubusercontent.com/276077/165425394-d7877396-700e-467a-9773-4df63b9c2ce6.png)

## templates/registration/logged_out.html
![image](https://user-images.githubusercontent.com/276077/165425538-bce0eda1-ce46-4680-b1ce-804821d8d464.png)

## templates/registration/login.html
![image](https://user-images.githubusercontent.com/276077/165425573-5f84b9cb-2898-46d1-bcf2-225ff5cfa32a.png)

## templates/registration/password_change_form_done.html
![image](https://user-images.githubusercontent.com/276077/165425603-62cb8885-3bb9-4e08-bfd1-57242aa27df0.png)

## templates/registration/password_change_form.html
![image](https://user-images.githubusercontent.com/276077/165425652-de36fbdf-37af-400d-a655-09173582e56d.png)

Todos os arquivos da pasta registration seguem o padrão de nome que são indicados pela documentação Django, uma vez que são templates que já serão procurados pelo 'django.contrib.auth'


https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
