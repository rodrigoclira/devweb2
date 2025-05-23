# Projeto com arquitetura Serverless (AWS Lambda + AWS API Gateway)

![image](https://user-images.githubusercontent.com/276077/118579345-48beab80-b764-11eb-83db-3f7a33eb4265.png)

Pré-requisitos:
- Ter acesso a uma conta da AWS com os serviços: Lambda e API Gateway

Objetivo: 
Neste projeto será criado uma API que realiza operações matemáticas simples (calculadora) utilizando o conceito de serverless com a utilização da AWS Lambda e API Gateway.

Passos para execução:

## Criando as funções lambdas

1. Acesse ao serviço Lambda da AWS e crie uma função lambda usando a opção "Usar um esquema". Pesquise e selecione o esquema: "hello world function". Dê um nome a função baseando-se nos exemplos disponíveis na pasta "lambdas" do repositório. Exemplo: soma 

![image](https://github.com/user-attachments/assets/4ff4e945-c79d-4502-9146-c7892caaa147)

2. Na tela de exibição da função criada, abra a aba "código" e substitua-o pelo código da função lambda do repositório. Se na etapa anterior foi criada a função "subtracacao", copie o conteúdo do arquivo "lambdas/subtracacao.py" .

![image](https://github.com/user-attachments/assets/2b24fd8f-3222-46d4-9057-6ca826e84578)

Novo código

![image](https://github.com/user-attachments/assets/088aa1c7-f6e0-4509-a73b-27d71bd13f4f)

3. Clique em "Implantar" ou "Deploy".
   
4. Repita os passos 1-2 para adicionar as outras funções lambdas. Os nomes delas serão: soma e calc.

5. No final, todas as três funções estarão criadas.

   ![image](https://github.com/user-attachments/assets/04380005-94d8-43fc-95b6-d71c51790cca)




-----------------------------------------------------



## Criando o Gateway (API-Gateway)

1. No serviço `API Gateway` da AWS, escolha o `HTTP API`, clicando em `Build`.
   
![image](https://github.com/user-attachments/assets/f7f63e56-6c75-4606-b04d-d561401c2aaf)

2. Dê um nome para a API e em seguida clique em `Add Integration` e adicione as funções lambdas `calc`, `soma` e `sub`. 
Depois clique em `Próximo`.

![image](https://github.com/user-attachments/assets/27d29bee-f2e3-48f1-898f-67d82b7b7c18)

3. Configure a rota, usando apenas o método `GET`, como na figura abaixo

![image](https://github.com/user-attachments/assets/e5f8149a-d02a-43ef-ac29-a83cd653b085)

4. Não modifique o estágio. Deixe o valor $default e auto-deploy.
   
![image](https://github.com/user-attachments/assets/e3c12454-6307-42f2-80e7-99edf0475fab)

5. Clique em criar.

![image](https://github.com/user-attachments/assets/452b7791-a5ef-4769-9e24-bca79cad63d0)

6. Em seguida clique em `Deploy`

![image](https://github.com/user-attachments/assets/5ca59bc9-63cb-4a88-8d49-60daed2d81e3)

7. Adicione um estágio de implantação.
   
![image](https://github.com/user-attachments/assets/fcc555cd-02e7-4ab1-9cee-5ff8ada7eb68)

8. Agora que tudo foi criado, você já pode usar o seu projeto criado na arquitetura serverless. 

Copie a url do *gateway* e adicione a rota que desejas acessar. Por exemplo: 

`https://URL_GATEWAY/{nome-do-stage}/calc`

`https://URL_GATEWAY/calc`

## Usando o POSTMAN ou INSOMNIA para testar a API 

- calc

![image](https://user-images.githubusercontent.com/276077/115634822-c071f580-a2e0-11eb-94a6-c7a8bc7bf58b.png)

![image](https://github.com/user-attachments/assets/ac762b7e-0f17-4449-b316-f02899df72c3)


- soma

![image](https://user-images.githubusercontent.com/276077/115634892-e4353b80-a2e0-11eb-84bc-0683f80b8eea.png)

![image](https://github.com/user-attachments/assets/01e5fa8d-3beb-4d16-8f10-c4efd4c1e285)


- subtracao

![image](https://user-images.githubusercontent.com/276077/115634940-0038dd00-a2e1-11eb-92b5-dc04ce523baf.png)

![image](https://github.com/user-attachments/assets/d0581be3-cdef-4c71-b592-968d2de7cb79)


## Que tal usar o S3 para criar um site estático? 

Use o tutorial [https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html)
