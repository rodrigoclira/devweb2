# Instalação do Code Server em Ubuntu Linux

Se você estiver usando o EC2, siga o passo a passo abaixo. Caso você esteja utilizando uma outra infraestrutura, pule para o Passo 7, onde é exibida a instalação do Code Server.

1. Clique em 'Iniciar Instância' 

<img width="1090" height="857" alt="image" src="https://github.com/user-attachments/assets/5400f8bb-9816-4e08-99be-b419b2e9b4fd" />

---

2. Indique um nome por exemplo: "DEV" e escolha a opção de SO: `Ubuntu Linux`


<img width="1082" height="847" alt="image" src="https://github.com/user-attachments/assets/71e5f75f-3116-4a84-8f07-ec8f9cc5ec1f" />

---

3. Escolha a instância `t3.large` e como o key pair: `vokey`
<img width="1085" height="411" alt="image" src="https://github.com/user-attachments/assets/d19824e1-b6df-4b52-95c2-3b77e924afa6" />

---

4. Em Configuração da Rede (configuração do firewall), marque as opções Permitir ssh, Permitir HTTPS e Permitir http. 
<img width="1070" height="356" alt="image" src="https://github.com/user-attachments/assets/1b12fc4a-c0e5-4d74-b3c1-9d0c6432e2ea" />

---

5. Na configuração de armazenamento, aumento o HD para 30GB. 
<img width="1089" height="299" alt="image" src="https://github.com/user-attachments/assets/67c373ad-3bcf-423f-b74f-a3a36bba2f1a" />

---

6. Crie a instância. 
<img width="547" height="136" alt="image" src="https://github.com/user-attachments/assets/24c2e92e-da26-4e9f-9a06-a7a0426e1ae5" />

---

7. Em seguida, após a inicialização (estado "running"), conecte-se à instância e cole o seguinte comando na linha de comando: 

> Essa instalação utiliza um certificado autoassinado, conforme descrito na documentação do projeto. 

```bash
echo "Installing code server..."

sudo apt update
curl -fsSL https://code-server.dev/install.sh | sh
sudo apt-get -y install python3-pip
sudo apt-get -y install python3.14-venv 

echo "Configuring code server..."
sudo systemctl enable --now code-server@$USER
sudo systemctl restart code-server@$USER
sleep 3

sed -i.bak 's/cert: false/cert: true/' ~/.config/code-server/config.yaml
sed -i.bak 's/bind-addr: 127.0.0.1:8080/bind-addr: 0.0.0.0:443/' ~/.config/code-server/config.yaml
sudo setcap cap_net_bind_service=+ep /usr/lib/code-server/lib/node
sed -i.bak 's/^password: .*/password: code/' ~/.config/code-server/config.yaml

sudo systemctl enable --now code-server@$USER

echo
echo "This is your configuration file"
echo
cat ~/.config/code-server/config.yaml

echo
echo "Restarting service..."
echo
sudo systemctl restart code-server@$USER
```
---

8. Após a instalação, acesse o Code Server utilizando o IP ou o DNS público da máquina virtual (disponível na aba Networking). 

<img width="1620" height="470" alt="image" src="https://github.com/user-attachments/assets/d1d915b2-d140-44c4-aadf-903634e71c61" />


# Referências
https://github.com/coder/code-server
