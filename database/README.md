# ORM e o NoSQL (MongoDB)

Este projeto tem como objetivo destacar a utilização do ORM do django e do NoSQL. 
<br>
Neste projeto o MongoDB é utilizado para persistir as informaçẽos dos comentários dos projetos.


## Pré-requisitos

> **Instalar bibliotecas** informadas no arquivo 'requirements.txt' 

```bash
pip3 install -r requirements.txt
```

> **Instalação do MongoDB**
> 
> Use o tutorial do site do MongoDB que seja compatível com o seu SO. 
> Link direto para o [Amazon Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/)

## Comandos

Incialize o daemon do MongoDB. 

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


## AWS

Replique o projeto utilizando uma instância do RDS e do DocumentDB na AWS.


## FAQ

### Erros Mongodb
Mongo não inicia, erro com status 14 < https://stackoverflow.com/questions/64608581/mongodb-code-exited-status-14-failed-but-not-any-clear-errors > 

![image](https://user-images.githubusercontent.com/276077/140451154-46459ade-85d0-4839-b24a-dca3c28df0d3.png)

```
chown -R mongod:mongod /var/lib/mongo/
chown mongod:mongod /tmp/mongodb-27017.sock

systemctl restart mongod
```
