# Passos para instalação na AWS com o Cloud9

1. Crie um ambiente com o Cloud9 (use a instância `t3.small`)

2. Abra o Cloud9 e copie os arquivos para a pasta principal, através da opção "File" -> "Upload Local File". 

![image](https://github.com/user-attachments/assets/d461d27f-fbb7-4b7b-be1a-8bbba5965e38)

3. Instale a biblioteca `libpq-dev` 

```
sudo apt install libpq-dev -y
```

4. Instale o [MongoDB](MONGO.md)

5. Em seguida, crie um ambiente virtual e ative-o:

![image](https://github.com/user-attachments/assets/0d1e8927-d6bb-4bc6-8e39-8dae8ec7727c)

```
python -m venv venv
source venv/bin/activate
```
6. Após ativar o ambiente, instale os pacotes indicados no arquivo `requirements.txt`.

![image](https://github.com/user-attachments/assets/e034c6e4-d317-47dd-9220-b529cc1c4fd4)

```
pip install -r requirements.txt 
```

7. Acesse a pasta `sgc` e execute o projeto Django


![image](https://github.com/user-attachments/assets/6a694ec1-3e17-46ae-ab9d-be7786f9ddde)

```
python manage.py runserver 0.0.0.0:8080
```

8. Clique em `Preview` e escolha `Preview Running Application` e em seguida `Pop out into new Window`.

![image](https://github.com/user-attachments/assets/9e8781a7-918f-4df6-9171-995700fd241c)

![image](https://github.com/user-attachments/assets/0724f536-bb1c-4e45-af27-d00068256dff)

9. Digite agora no navegador:

`https://URL-DO-CLOUD9/projeto`

![image](https://github.com/user-attachments/assets/4379f9a3-50a3-47b0-bb5a-ae484786f62e)


## Banco de dados na AWS

Pesquise e em seguida, altere o projeto para utilizar os serviços de banco de dados gerenciados da AWS.

> Confirmar se todos os serviços estão disponíveis no Learner Lab. 

1. RDS (Banco de Dados Relacional)

2. DocumentDB (MongoDB)

Mais informações sobre os banco de dados da AWS: https://aws.amazon.com/products/databases/

![image](https://github.com/user-attachments/assets/badca81c-ca9b-406b-8037-e97cc63fb693)



