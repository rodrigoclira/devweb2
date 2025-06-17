# Passos para instalação na AWS com o Cloud9

1. Crie um ambiente com o Cloud9

3. Abra o Cloud9 e copie os arquivos para a pasta principal, através da opção "File" -> "Upload Local File". 

![image](https://github.com/user-attachments/assets/d461d27f-fbb7-4b7b-be1a-8bbba5965e38)

3. Em seguida, crie um ambiente virtual e ative-o:

![image](https://github.com/user-attachments/assets/0d1e8927-d6bb-4bc6-8e39-8dae8ec7727c)

```
python -m venv venv
source venv/bin/activate
```
4. Após ativar o ambiente, instale os pacotes indicados no arquivo `requirements.txt`.

![image](https://github.com/user-attachments/assets/e034c6e4-d317-47dd-9220-b529cc1c4fd4)

```
pip install -r requirements.txt 
```

5. Acesse a pasta `sgc` e execute o projeto Django


![image](https://github.com/user-attachments/assets/6a694ec1-3e17-46ae-ab9d-be7786f9ddde)

```
python manage.py runserver 0.0.0.0:8080
```


6. Clique em `Preview` e escolha `Preview Running Application` e em seguida `Pop out into new Window`.

![image](https://github.com/user-attachments/assets/9e8781a7-918f-4df6-9171-995700fd241c)

![image](https://github.com/user-attachments/assets/0724f536-bb1c-4e45-af27-d00068256dff)

8. Digite agora no navegador:

`https://URL-DO-CLOUD9/projeto`

![image](https://github.com/user-attachments/assets/4379f9a3-50a3-47b0-bb5a-ae484786f62e)
