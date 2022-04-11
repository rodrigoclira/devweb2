# Descrição do Projeto


Nesta aula serão apresentandos três projetos utilizando arquiteturas distintas: monolítico, microserviços, serverless, hibrida e pub-sub. 
Os projetos desenvolvidos nas arquiteturas monolítica, microsserviços, serverless e hibrida simulam uma API pública que expõe três endpoints /calc /sub e /soma. 

Exemplo de chamadas da API projeto monolítico
```
GET http://127.0.0.1:8000/api/calc

GET http://127.0.0.1:8000/api/soma?op1=100&op2=20

GET http://127.0.0.1:8000/api/sub?op1=1002&op2=20
```


O projeto desenvolvido na arquitetura pub/sub simula um projeto de manipulação de imagem. O usuário realiza o upload de uma imagem e dois outros microsserviços (grayscale e rotate) realizam o processamento dela. 
