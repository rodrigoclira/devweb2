# Projeto de exemplo da utilização do ORM e o NoSQL (MongoDB)

Este projeto tem como objetivo destacar a utilização do ORM do django e do NoSQL. Ele representa uma aplicação no qual os professores da instituição poderão listar os
seus projetos institucionais. Ao longo do curso, a aplicação irá evoluindo para apresentar outros conceitos abordados na disciplina. 
<br>
Neste projeto o MongoDB é utilizado para persistir as informaçẽos dos comentários dos projetos.


## Pré-requisitos
| Instalar dependências informadas no arquivo 'requirements.txt' 

| Instalação do MongoDB

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

