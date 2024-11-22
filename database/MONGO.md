# Instalação do MONGO DB no Ubuntu 22.04

## Instalar MongoDB Community Edition

Siga estes passos para instalar o MongoDB Community Edition usando o gerenciador de pacotes apt.


1. Importar a chave pública.
Em um terminal, instale gnupg e curl se eles ainda não estiverem disponíveis:


```
sudo apt-get install gnupg curl
```

Para importar a chave pública GPG do MongoDB, execute o seguinte comando:

```
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
```

2. Criar o arquivo de lista.
Crie o arquivo de lista /etc/apt/sources.list.d/mongodb-org-8.0.list para sua versão do Ubuntu.

```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```
3. Recarregar o banco de dados de pacotes.
Execute o seguinte comando para recarregar o banco de dados local de pacotes:

```
sudo apt-get update
```

4. Instalar o MongoDB Community Server.
Você pode instalar tanto a última versão estável do MongoDB quanto uma versão específica.
Para instalar a última versão estável, execute o seguinte comando:

```
sudo apt-get install -y mongodb-org
```

Para ajuda com a solução de problemas encontrados durante a instalação do MongoDB no Ubuntu, consulte nosso guia de solução de problemas.

## Executar MongoDB Community Edition

1. Iniciar MongoDB.
Você pode iniciar o processo mongod executando o seguinte comando:

```
sudo systemctl start mongod
```

## Acessando o Mongo

1. Inicie o mongosh

```
mongosh
```

2. Mude para a coleção `comments`

```
use comments;
```

3. Procure pelos documentos
```
db.comentario.find()
```

![image](https://github.com/user-attachments/assets/63832e5a-229f-46fd-8191-78ba155a25bf)


Baseado em: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
