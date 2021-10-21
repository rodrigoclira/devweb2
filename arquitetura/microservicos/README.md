# Projeto usando a arquitetura Microserviços (Flask + Docker)

![image](https://user-images.githubusercontent.com/276077/116923013-77009f00-ac2c-11eb-859b-735835360d09.png)


## Pré-Requisitos: 
| [Docker](https://docs.docker.com/engine/install)


O passo a passo segue o que é apresentado tutorial apresentado em: [Building a Python scalable Flask application using docker-compose and Nginx load balancer
](https://www.linkedin.com/pulse/building-python-scalable-flask-application-using-nginx-itay-melamed/)

Algumas alterações foram realizadas para que o projeto ficasse com as mesmas funcionalidades das apresentadas nos projetos de arquitetura serverless e monolítica (API de soma, sub e calc). Para fins de discussão sobre a funcionalidade de *Load Balancing*, o projeto "app" apresentado no tutorial foi mantido.


Para executá-lo, basta baixar a pasta do projeto (microservicos) e executar o comando "docker-compose up" na pasta principal. 

```
$ sudo docker-compose up --build -d --scale app=2
```

![image](https://user-images.githubusercontent.com/276077/116919459-ab259100-ac27-11eb-8edb-5bd0f81f701e.png)

O comando cria, inicia e anexa containers em um serviço. O parâmetro --build força o construção da imagem antes da criação do serviço, o parâmetro -d faz com que os containers sejam executados em backgroud, e por fim, o --scale informa a quantidade de containers de um determinado serviço, sobrescrevendo o valor informado no compose-file.

Mais informações do docker-compose no [link](https://docs.docker.com/compose/reference/down/)

Para saber se todos os serviços estão rodando, pode-se utilizar o comando: 

```
sudo docker ps --format '{{.Names}}'
``` 

Se tudo estiver ocorrido da forma esperada, o resultado será algo assim: 
![image](https://user-images.githubusercontent.com/276077/116919942-6817ed80-ac28-11eb-8fc5-b9ee7b335b2c.png)

Ainda é possível analisar cada um dos logs gerados pelas aplicações no container usando o comando "docker logs". 

```
sudo docker logs nginx -f
```

Nesse caso analisando o serviço (container) nginx. 

![image](https://user-images.githubusercontent.com/276077/116920240-c2b14980-ac28-11eb-9150-b20f653ccb70.png)

Agora é só usar o postman para fazer as requisições. Exemplo de requisição para a funcionalidade de soma

![image](https://user-images.githubusercontent.com/276077/116920423-fdb37d00-ac28-11eb-8ad3-1517aaedeb52.png)

Por fim, o comando 'docker-compose down' derruba todos os serviços. 

```
sudo docker-compose down
```

![image](https://user-images.githubusercontent.com/276077/116920668-4f5c0780-ac29-11eb-8905-dadc80b5fe62.png)

## Outros projetos usando Microserviços

- https://github.com/rodrigoclira/micro-livraria
- https://github.com/rodrigoclira/microservice-WEB2

