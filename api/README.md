# Exemplo de projeto usando Django Rest Framework e SimpleJWT

Nesse projeto, além do acesso via web, é disponibilizada uma API que permite ao usuário obter informações da aplicação. 

Após instalar as dependências, execute o comando abaixo para rodar o programa: 
```
python manage.py runserver 
```

no Cloud9 use o comando
```
python manage.py runserver 0.0.0.0
```

Requisições usando o curl no EC2/Cloud9

## Listando todos os projetos
```
curl http://localhost:8080/api/projetos/
```
<img width="1093" height="935" alt="image" src="https://github.com/user-attachments/assets/e919bf3c-0f61-4f42-80c3-c8a608d59871" />

## Obtendo o token de autenticação
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}' \
  http://localhost:8080/api/token/
```
<img width="1093" height="935" alt="image" src="https://github.com/user-attachments/assets/9d57ae22-c003-425b-9ab8-879bf5c8ec6d" />

Não esqueça de configurar o header `Content-Type: application/json`, como na imagem abaixo. 

<img width="1098" height="176" alt="image" src="https://github.com/user-attachments/assets/d06a42be-1aed-49fd-97f2-b7fc47f8b1de" />

## Obtendo os detalhes de um projeto
```
curl \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYzMzUyMzQwLCJqdGkiOiIzYmE5ZjJiMDYwY2Q0NDU0ODFlMmQ3MmRhYmExMzg4NiIsInVzZXJfaWQiOjF9.VEk6Nuxa8UhCtaRWNA_Eb-FzhxBdC0brePWbA9u-PwY" \
  http://localhost:8080/api/projetos/1
```

<img width="1093" height="935" alt="image" src="https://github.com/user-attachments/assets/9b837314-0ca3-4138-8c3c-350df8d903d7" />



https://www.freecodecamp.org/news/graphql-vs-rest-api/
