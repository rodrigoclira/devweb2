
# Etapas para execução da aplicação Django

Acessar a pasta do projeto
```
cd Django-Poll-App/
```

Criar e posteriormente ativar o ambiente virtual
```
python3 -m venv venv
source venv/bin/activate
```

Instalar as dependências
```
pip3 install -r requirements.txt
```

Criar base de dados e executar migrações
```
python manage.py makemigrations
python manage.py migrate
```

Executar o projeto na porta 8080
```
python manage.py runserver 0.0.0.0:8080
```


Como criar um super usuário (admin)?
```
python manage.py createsuperuser
```
