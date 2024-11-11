# Projeto usando padrão Publish/Subscribe (Flask + Docker + Apache Kafka)


![image](https://user-images.githubusercontent.com/276077/162766448-13e0ebe8-8325-4e32-a8d7-5deff7744c10.png)


## Pré-Requisitos: 
| Instalação do [Docker](https://docs.docker.com/engine/install)

| Instalação do [Docker Compose](https://docs.docker.com/compose/install/)


Antes de começar, vamos entender alguns conceitos importantes sobre o Kafka:

* **Kafka cluster**: Um sistema distribuído de clusters kafka

* **Kafka broker**: O message broker responsável por mediar os dados entre os produtores e os consumidores. Eles são responsáveis por juntar as operações de I/O e persistir isso no cluster.

* **ZooKeeper**: Gerencia todo controle do cluster. Ele age como um repositório de configuração, mantendo os metadados do cluster e também implementando os mecanismo do cluster. 

* **Kafka producer**: Aplicação cliente responsável por adicionar registros nos tópicos do Kafka.

* **Kafka consumer**: Aplicação que ler os tópicos. 

O exemplo exibe um projeto que utiliza microsserviços e o apache kafka. O apache kafka funciona como um intermediador para transmitir mensagens publicadas no tópico '_image_' pelo microsserviço 'upload' para os microsserviços 'rotate' e 'grayscale'. Ao serem notificados, esses microsserviços realizam operações em arquivos de imagem que estão salvos num volume compartilhado. 

Para executá-lo, basta baixar a pasta do projeto (pub-sub) e executar o comando "docker-compose up" na pasta principal. 

```
sudo docker-compose up --build 
```

![image](https://user-images.githubusercontent.com/276077/162104971-34cde74b-c4f7-4da5-a2da-d18176780838.png)
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
sudo docker logs -f
```



Acessando o KafDrop em ```localhost:9000```

> “Kafdrop is a web UI for viewing Kafka topics and browsing consumer groups. The tool displays information such as brokers, topics, partitions, consumers, and lets you view messages.” — [Kafdrop on GitHub](https://github.com/obsidiandynamics/kafdrop)

![image](https://user-images.githubusercontent.com/276077/162105063-717094f5-5f10-478d-ac4b-3c20fd7350b2.png)

Visualizando os tópicos

![image](https://user-images.githubusercontent.com/276077/162105269-32fce2fd-363e-4393-85c2-951fd4ac9639.png)




Por fim, o comando 'docker-compose down' derruba todos os serviços. 

```
sudo docker-compose down
```
## Atividade novo consumidor

![image](https://github.com/user-attachments/assets/00f21461-7345-45e4-9d08-38763657465a)

Baseando-se no código indicado em [https://gist.github.com/rodrigoclira/9e1be73222f16248a59b1389905b1d6c](https://gist.github.com/rodrigoclira/9e1be73222f16248a59b1389905b1d6c), crie um novo consumidor que irá escrever o nome do arquivo na imagem. Ao final, do upload, os três microsserviços serão notificados para que realizem suas respectivas operações.


## Atividade novo(s) tópico(s)

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

* Telegram: 
   * https://usp-python.github.io/05-bot/
   * https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key
  
* E-mail:
   * https://realpython.com/python-send-email/

Ao terminar os experimentos, lembre-se de executar ```docker-compose down```

## Artigos que foram base para o projeto

- Exemplo de código com Kafka < https://betterprogramming.pub/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9 >

- Exemplo de programa em Flask com upload de imagem < https://github.com/roytuts/flask/tree/master/python-flask-upload-display-image >

## Projetos Relacionados
- [Pub Sub Store](https://github.com/rodrigoclira/pub-sub-store)

## Material Complementar

[Arquitetura Publish/Subscribe](https://engsoftmoderna.info/cap7.html#arquiteturas-publishsubscribe)

[Entendo o Kafka](https://vepo.medium.com/entendendo-o-kafka-bf64169e421f)

[Apache Kafka](https://medium.com/trainingcenter/apache-kafka-838882261e83)

[Apache Kafka: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
