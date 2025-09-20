# Projeto usando a arquitetura Microserviços (Flask + Docker)

![image](https://user-images.githubusercontent.com/276077/116923013-77009f00-ac2c-11eb-859b-735835360d09.png)


## Pré-Requisitos: 
| Instalação do [Docker](https://docs.docker.com/engine/install)

| Instalação do [Docker Compose](https://docs.docker.com/compose/install/)


O passo a passo segue o que é apresentado tutorial apresentado em: [Building a Python scalable Flask application using docker-compose and Nginx load balancer
](https://www.linkedin.com/pulse/building-python-scalable-flask-application-using-nginx-itay-melamed/)

Algumas alterações foram realizadas para que o projeto ficasse com as mesmas funcionalidades das apresentadas nos projetos de arquitetura serverless e monolítica (API de soma, sub e calc). Para fins de discussão sobre a funcionalidade de *Load Balancing*, o projeto "ping" apresentado no tutorial foi mantido.


Para executá-lo, basta baixar a pasta do projeto (microserviços) e executar o comando "docker-compose up" na pasta principal. 

```
sudo docker-compose up --build -d --scale ping=2
```

![image](https://user-images.githubusercontent.com/276077/116919459-ab259100-ac27-11eb-8edb-5bd0f81f701e.png)

O comando cria, inicia e anexa containers em um serviço. O parâmetro --build força a construção da imagem antes da criação do serviço, o parâmetro -d faz com que os containers sejam executados em background, e por fim, o --scale informa a quantidade de containers de um determinado serviço, sobrescrevendo o valor informado no compose-file.

Mais informações do docker-compose no [link](https://docs.docker.com/compose/reference/down/)

Para saber se todos os serviços estão rodando, pode-se utilizar o comando: 

```
sudo docker ps --format '{{.Names}}'
``` 

Se tudo estiver ocorrido da forma esperada, o resultado será algo assim: 
![image](https://user-images.githubusercontent.com/276077/116919942-6817ed80-ac28-11eb-8fc5-b9ee7b335b2c.png)

### Visualizando os logs dos _containers_

Ainda é possível analisar cada um dos logs gerados pelas aplicações no container usando o comando "docker logs". 

```
sudo docker logs nginx -f
```
ou visualizar todos os logs de uma única vez com: 

```
sudo docker-compose logs -f
```

Nesse caso, analisando o serviço (container) nginx. 

![image](https://user-images.githubusercontent.com/276077/116920240-c2b14980-ac28-11eb-9150-b20f653ccb70.png)

### Utilizando o Postman ou Insomnia

Agora é só usar o Postman para fazer as requisições. Exemplo de requisição para a funcionalidade de soma

![image](https://user-images.githubusercontent.com/276077/116920423-fdb37d00-ac28-11eb-8ad3-1517aaedeb52.png)

### Desligando os _containers_
Por fim, o comando 'docker-compose down' derruba todos os serviços. 

```
sudo docker-compose down
```

![image](https://user-images.githubusercontent.com/276077/116920668-4f5c0780-ac29-11eb-8905-dadc80b5fe62.png)

## Troubleshooting

### Erro ao iniciar o container do nginx (porta já utilizada)

Modifique no docker-compose.yml a porta que será exposta pelo nginx. Utilize a porta 8080. 

```
ports:
- 8080:80
```

### Problema no acesso "VFS connection does not exist"
Se você estiver rodando o projeto no Cloud9, o acesso à url de _preview_ fica disponível apenas no mesmo navegador, impossibilitando o teste usando o Postman ou Insomnia.
https://docs.aws.amazon.com/cloud9/latest/user-guide/app-preview.html#app-preview-preview-app

Caso precise acessar essas aplicações para testar a aplicação, altere o `Segurity Group` do EC2 utilizado pelo seu ambiente Cloud9. Nessa alteração você deve permitir o acesso a porta utilizada no `docker-compose`. Em seguida, para fazer o teste de acesso é necessário utilizar o dns público da máquina EC2. 


## Atividade

Adicione um novo microserviço à arquitetura atual do exemplo. Ele será responsável pelo novo *endpoint* da api que realiza uma multiplicação (**/mult**). Ele receberá dois valores, **op1**, **op2** e retornará o resultado da multiplicação. Você precisa criar uma nova aplicação com um outro framework (não utilizar Flask).

Devido a sua alta demanda de acesso, o microserviço precisa ser replicado em 3 contêineres. A distribuição será feita através da política de balanceamento de carga *Round Robin* com diferentes pesos e funções. Um contêiner deve ser configurado como **backup** e os outros dois com o peso 3 e 1, respectivamente. Para mais informações sobre distribuição de peso, acesse: https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/ (*Seção Server Weights*).

Reponda as seguintes perguntas abaixo após desenvolver as modificações necessárias para que esses novos requisitos sejam alcançados. 

1. Como é feita a distribuição das requisições para o endpoint **/mult** ? Discorra sobre o que acontece. (use Postman, Isomnia, thunder client...)

2. O que acontece quando os containers da aplicação **mult** param de funcionar? 
Para simular esse cenário [use o *docker stop nome_container* para parar containers](https://medium.com/xp-inc/principais-comandos-docker-f9b02e6944cd). Pare cada um dos containers que estão recebendo requisição da aplicação **mult** por vez e analise o que está acontecendo. 
> O container de **backup** não deve ser parado. 

Ao terminar os experimentos, lembre-se de executar ```docker-compose down```



## Projetos Relacionados

- [Micro Livraria](https://github.com/rodrigoclira/micro-livraria)
- [Projeto da Disciplina (2021.1)](https://github.com/rodrigoclira/microservice-WEB2)

##  Material Complementar

- [GRPC ou API Rest ?](https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)

- [GRPC com Python](https://realpython.com/python-microservices-grpc)

- [Vídeo 'Docker e Docker Compose na Prática'](https://www.youtube.com/watch?v=YlYTnRRDRyM)

- [Vídeo 'Como Rodar Docker na EC2'](https://www.youtube.com/watch?v=TU3P1fYcTyc)
