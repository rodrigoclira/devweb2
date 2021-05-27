# Projeto com arquitetura Serverless (AWS Lambda + AWS API Gateway)

![image](https://user-images.githubusercontent.com/276077/118579345-48beab80-b764-11eb-83db-3f7a33eb4265.png)

Pré-requisitos:
- Ter acesso a uma conta da AWS com os serviços: Lambda e API Gateway


Objetivo: 
Neste projeto será criado uma API que realiza operações matemáticas simples (calculadora) utilizando o conceito de serverless com a utilização da AWS Lambda e API Gateway.

Passos para execução:

1. Acesse ao serviço Lambda da AWS e crie uma função lambda usando a opção "Usar um esquema". Pesquise e selecione o esquema: "hello-world-python". Ao selecionar o equema, clique em "Configurar".
![image](https://user-images.githubusercontent.com/276077/115634586-4a6d8e80-a2e0-11eb-826e-b9dc4da2f103.png)

2. Dê um nome a função baseando-se nos exemplos disponíveis na pasta "lambdas" do repositório. Exemplo: soma 
![image](https://user-images.githubusercontent.com/276077/115634711-830d6800-a2e0-11eb-98b4-dcdc9d1499a0.png)

3. Na tela de exibição da função criada, abra a aba "código" e substitua o código atual pelo código da função lambda do repositório. Se na etapa anterior foi criada a função "soma", copie o conteúdo do arquivo "lambdas/soma.py" .
![image](https://user-images.githubusercontent.com/276077/115634481-14c8a580-a2e0-11eb-89bb-eebe285239fb.png)

4. Se for a primeira lambda criada, na parte superior, clique em "Adicionar um Gatilho". 

5. Escolha "API Gateway" e preencha as seguintes informações:
	- Tipo: API HTTP
	- Segurança: Abrir
	- Em configurações adicionais:
		- Nome da API: API-HTTP
		
6. Repita os passos 1-3 para adicionar as outras funções lambdas. Os nomes delas serão: subtracao e calc.

7. Para adicionar o gatilho das novas funções, vá até o console do API Gateway e selecione o gateway criado ("API HTTP"). Para ir até o console do API Gateway é necessário acessar o serviço "API Gateway" da AWS. 

8. No painel esquerdo, clique em "Rotas". Deverá ser exibida o nome da primeira função lambda criada. Ex.: /soma

9. Clique em "Create" e adicione novas rotas, sendo elas os nomes das funções lambdas já criadas. Ex.: /calc, /subtracao

10. Agora no campo de "Integrações", no painel esquerdo. Clique em "Gerenciar Integrações" e em "Create". No campo Anexar essa integração a uma rota, escolha uma das rotas criadas no passo anterior. No campo "Destino da Integração", escolha "Função Lambda" e em detalhes, selecione o lambda correspondente. Faça esse procedimento para todas as funções lambdas criadas no passo 6.


Agora que tudo foi criado, você já pode usar o seu projeto criado na arquitetura serverless. 

Pegue a url do gateway* e coloque a rota que desejas acessar. Por exemplo: 

https://URL_GATEWAY/calc

Essa informação também fica disponível nas lambdas 
![image](https://user-images.githubusercontent.com/276077/115634404-f4005000-a2df-11eb-9cf4-b57d2b336edc.png)

* A URL do gateway pode ser obtida na página inicial do serviço "API GATEWAY" da Amazon. 
![image](https://user-images.githubusercontent.com/276077/117976655-67f1af00-b306-11eb-8491-08e7c765b72f.png)


## USando o POSTMAN para testar a API

- calc

![image](https://user-images.githubusercontent.com/276077/115634822-c071f580-a2e0-11eb-94a6-c7a8bc7bf58b.png)


- soma

![image](https://user-images.githubusercontent.com/276077/115634892-e4353b80-a2e0-11eb-84bc-0683f80b8eea.png)


- subtracao

![image](https://user-images.githubusercontent.com/276077/115634940-0038dd00-a2e1-11eb-92b5-dc04ce523baf.png)


| Sugestão de conteúdo

[Serverless Design with AWS Lambda](https://amazon.qwiklabs.com/quests/17)
