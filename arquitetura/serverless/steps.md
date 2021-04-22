# Usando o AWS Lambda e o AWS API Gateway 

Pré-requisitos:
- Ter acesso a uma conta da AWS com os serviços: Lambda e API Gateway


Objetivo: 
Neste projeto será criado uma API que realiza operações matemáticas simples (calculadora) utilizando o conceito de serverless com a utilização da AWS Lambda e API Gateway.

Passos para execução:

1. Criar uma função lambda usando a opção "Usar um esquema". Pesquise e selecione o esquema: "hello-world-python". 

2. Dê um nome a função baseando-se nos exemplos disponíveis na pasta "lambda" do projeto. Exemplo: soma 

3. Na tela de exibição da função criada, abra a aba "código" e substitua o código atual pelo código da função lambda do projeto. Se na etapa anterior foi criada a função "soma", copie o conteúdo do arquivo lambda/soma.py .

4. Se for a primeira lambda criada, na parte superior, clique em Adicionar um Gatilho. 

5. Escolha API Gateway e preencha as seguintes informações:
	- Tipo: API HTTP
	- Segurança: Abrir
	Em configurações adicionais:
		- Nome da API: HTTP-API
		
6. Repita os passos 1-3 para adicionar as outras funções lambdas.

7. Para adicionar o gatilho, vá até o console do API Gateway e selecione o gateway criado.

8. No painel esquerdo, clique em "Rotas". Deverá ser exibida o nome da primeira função lambda criada. Ex.: /soma

9. Clique em Create e adicione novas rotas, sendo elas os nomes das funções lambdas já criadas.

10. Agora no campo de "Integrações", no painel esquerdo. Clique em "Gerenciar Integrações". No campo Anexar essa integração a uma rota, escolha uma das rotas criadas no passo anterior. No campo "Destino da Integração", escolha "Função Lambda" e em detalhes, selecione o lambda correspondente. 
