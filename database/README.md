# ORM e o NoSQL (MongoDB)

Este projeto tem como objetivo destacar a utilização do ORM do django e do NoSQL. 
<br>
Neste projeto o MongoDB é utilizado para persistir as informaçẽos dos comentários dos projetos.


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

![image](https://github.com/user-attachments/assets/1a043263-ee4d-4ab4-a811-c25823510096)


## FAQ

### Erros Mongodb
Mongo não inicia, erro com status 14 < https://stackoverflow.com/questions/64608581/mongodb-code-exited-status-14-failed-but-not-any-clear-errors > 

![image](https://user-images.githubusercontent.com/276077/140451154-46459ade-85d0-4839-b24a-dca3c28df0d3.png)

Comandos necessários

```
sudo chown -R mongod:mongod /var/lib/mongo/
sudo chown mongod:mongod /tmp/mongodb-27017.sock

sudo systemctl daemon-reload
```
## Atividade

Usando uma ORM com a framework escolhida, crie os models para representar o mini-mundo apresentado na imagem abaixo: 

![mini-mundo](https://user-images.githubusercontent.com/276077/163811963-bc1325ed-5321-42ce-bc24-b04426f3279b.png)

Considere as seguintes informações: 
- Atributos iniciadas com _dt-_ representam tipos de data. 
- O atributo com o nome _cod_ é do tipo numérico. 
- E-mail é um _varchar_ com validação (quando existente na ORM). 
- Todos os outros tipos são do tipo _varchar_. 

## Referências 
[SQL vs NoSQL, qual usar?
](https://www.treinaweb.com.br/blog/sql-vs-nosql-qual-usar#:~:text=O%20NoSQL%20%C3%A9%20mais%20indicado,flex%C3%ADvel%20no%20suporte%20de%20dados.)

[SQL ou NoSQL: eis a questão!!
](https://imasters.com.br/banco-de-dados/sql-ou-nosql-eis-a-questao)

[Como escolher entre SQL e NoSQL](https://pt.stackoverflow.com/questions/122452/como-escolher-entre-nosql-e-sql)

[Banco de Dados NoSQL: Um manual prático e didático](https://blog.geekhunter.com.br/banco-de-dados-nosql-um-manual-pratico-e-didatico/)
