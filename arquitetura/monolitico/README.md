# Projeto com Arquitetura Monolítica (Django) 


## Pré-requisitos
| Instalar dependências informadas no arquivo 'requirements.txt' 


Para executar projeto django utilize o seguinte comando: 


```
$ python manage.py runserver
```

## Executar na AWS

Instalação de pacotes
```
sudo apt-get update
sudo apt-get install python3-venv unzip -y
```

Download do repositório
```
wget  https://github.com/rodrigoclira/devweb2/archive/refs/heads/main.zip
```

Descompactar repositório
```
unzip main.zip
```
Acessar pasta do repositório

```
cd devweb2-main/arquitetura/monolitico/calcapi
```

Criando e ativando um ambiente virtual chamado `venv`
```
python3 -m venv venv
source venv/bin/activate
```

Instalando o arquivo de requirements do projeto
```
pip3 install -r requirements-monolitico.txt
```

Realizando as migrações
```
python manage.py makemigrations
python manage.py migrate
```

Rodando o servidor
```
python manage.py runserver 0.0.0.0:8000
```

Caso a porta 8000 não esteja disponível, execute na porta 80 seguinto os comandos abaixos:
```
sudo su
source venv/bin/activate
python manage.py runserver 0.0.0.0:80

```

Endpoints disponíveis
- http://DNS_AWS:PORTA/api/calc
- http://DNS_AWS:PORTA/api/soma
- http://DNS_AWS:PORTA/api/sub

