## Executar na AWS

1. Instalação de pacotes
```
sudo apt-get update
sudo apt-get install docker-compose unzip nginx -y
```


2. Download do repositório
```
wget  https://github.com/rodrigoclira/devweb2/archive/refs/heads/main.zip
```

3. Descompactar repositório
```
unzip main.zip
```

4. Acessar pasta do repositório
```
cd devweb2-main/arquitetura/pub-sub
```

5. Removendo configuração anterior
```
sudo rm /etc/nginx/sites-enabled/default
```

6. Copiando a configuração do proxy para a pasta do nginx. O proxy é necessário uma vez que na rede do IFPE não é permitido acessar todas as portas do projeto
```
sudo cp server-config/pub_sub /etc/nginx/sites-enabled/ -v
```

7. Restartando o nginx
```
sudo systemctl restart nginx
```

Siga o passo a passo do README
