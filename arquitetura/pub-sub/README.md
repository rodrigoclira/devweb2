# Projeto usando padrão PUB-SUB (Flask + Docker + Apache Kafka)


## Pré-Requisitos: 
| Instalação do [Docker](https://docs.docker.com/engine/install)

| Instalação do [Docker Compose](https://docs.docker.com/compose/install/)


O exemplo mostra um projeto que utiliza microsserviços e o apache kafka. O apache kafka funciona como um broker para transmitir mensagens publicadas no tópico 'imagem' pelo microsserviço 'upload' para os microsserviços 'rotate' e 'grayscale'. Ao serem notificados, esses microsserviços realizam operações em arquivos de imagem que estão salvos num volume compartilhado. 

Para executá-lo, basta baixar a pasta do projeto (pub-sub) e executar o comando "docker-compose up" na pasta principal. 

```
$ sudo docker-compose up --build 
```

![image](https://user-images.githubusercontent.com/276077/116919459-ab259100-ac27-11eb-8edb-5bd0f81f701e.png)

O comando cria, inicia e anexa containers em um serviço. O parâmetro --build força o construção da imagem antes da criação do serviço.

Mais informações do docker-compose no [link](https://docs.docker.com/compose/reference/down/)

Para saber se todos os serviços estão rodando, pode-se utilizar o comando: 

```
sudo docker ps --format '{{.Names}}'
``` 

Se tudo estiver ocorrido da forma esperada, o resultado será algo assim: 
![image](https://user-images.githubusercontent.com/276077/116919942-6817ed80-ac28-11eb-8fc5-b9ee7b335b2c.png)

Ainda é possível analisar cada um dos logs gerados pelas aplicações no container usando o comando "docker logs". 

```
sudo docker logs pub-sub_rotate_1 -f
```


Por fim, o comando 'docker-compose down' derruba todos os serviços. 

```
sudo docker-compose down
```

## Atividade

Adicione uma novo ator (microsserviço) no projeto que será responsável por notificar através do telegram ou e-mail que a operação do 'rotate' ou 'grayscale' foi finalizada. Para isso será necessário alterar o projeto adicionando uma nova etapa de pubicação num novo tópico (por exemplo **/notificacao**) por parte do microsserviço 'rotate' e 'grayscale'. O novo microsserviço '**notifacador**' será responsável por checar (pooling) o tópico e fazer o envio de mensagem no telegram ou e-mail para um contato defindo (pode ser fixo ou variável**) quando a operação estiver finalizada. 
** Se fizer variável, coloque um input de e-mail/telegram_id no HTML do microsserviço 'upload'. 

As mensagens enviadas devem conter:
  1. o nome do arquivo original
  2. a indicação da operação realizada

Por exemplo: 
```
O arquivo perfil.jpg foi rotacionado.
```
```
O arquivo perfil.jpg foi transformado em preto e branco.
```



Sugestões de como usar Telegram/Email: 

  Telegram: 
    https://usp-python.github.io/05-bot/
    https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key
  
  E-mail:
    https://realpython.com/python-send-email/

Ao terminar os experimentos, lembre-se de executar ```docker-compose down```


## Artigos que foram base para o projeto

- Exemplo de código com Kafka < https://betterprogramming.pub/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9 >

- Exemplo de programa em Flask com upload de imagem < https://github.com/roytuts/flask/tree/master/python-flask-upload-display-image >
