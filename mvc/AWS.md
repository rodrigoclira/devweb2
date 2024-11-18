# Passos para instalação na AWS 

1. Crie um ambiente com o Cloud9

2. Abra o Cloud9 e copie os arquivos para a pasta principal, através da opção "File" -> "Upload Local File". 

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
