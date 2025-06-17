# Exemplo Django OTP

Uma aplicação Django abrangente demonstrando autenticação por Senha Única Baseada em Tempo (TOTP) usando django-otp. Este exemplo apresenta segurança de nível empresarial com autenticação de dois fatores.

## Funcionalidades

- **Registro e Autenticação de Usuário**: Sistema completo de gerenciamento de usuários
- **Integração TOTP**: Suporte a Senha Única Baseada em Tempo usando django-otp
- **Geração de Código QR**: Geração automática de código QR para aplicativos autenticadores
- **Interface Moderna**: Interface bonita e responsiva com estilo Bootstrap
- **Recursos de Segurança**: Proteção CSRF, gerenciamento seguro de sessão
- **Visualizações Protegidas por OTP**: Demonstração de proteção de conteúdo sensível

## Stack Tecnológico

- **Backend**: Django 5.2.3
- **Biblioteca OTP**: django-otp 1.6.0
- **Códigos QR**: qrcode[pil] 8.2
- **TOTP**: pyotp 2.9.0
- **Frontend**: Bootstrap 5.3, Font Awesome 6.0
- **Banco de Dados**: SQLite (desenvolvimento)

## Instalação e Configuração

### Pré-requisitos

- Python 3.11+
- Gerenciador de pacotes pip

### Início Rápido

1. **Clone e navegue até o projeto**:
   ```bash
   cd django_otp_example
   ```

2. **Instale as dependências**:
   ```bash
   pip install django django-otp qrcode[pil] pyotp
   ```

3. **Execute as migrações**:
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

5. **Acesse a aplicação**:
   Abra seu navegador e navegue para `http://localhost:8000`

## Estrutura da Aplicação

```
django_otp_example/
├── otp_project/
│   ├── settings.py          # Configuração do Django
│   ├── urls.py             # Roteamento principal de URLs
│   └── wsgi.py             # Configuração WSGI
├── authentication/
│   ├── models.py           # Modelos de perfil de usuário e OTP
│   ├── views.py            # Visualizações de autenticação e OTP
│   ├── forms.py            # Formulários personalizados para auth e OTP
│   ├── urls.py             # Padrões de URL do app
│   └── migrations/         # Migrações do banco de dados
├── templates/
│   ├── base.html           # Template base com estilo
│   └── authentication/     # Templates específicos do app
│       ├── home.html       # Página inicial
│       ├── register.html   # Registro de usuário
│       ├── login.html      # Login de usuário
│       ├── dashboard.html  # Painel do usuário
│       ├── otp_setup.html  # Configuração OTP
│       ├── otp_verify.html # Verificação OTP
│       └── secure.html     # Conteúdo protegido
├── manage.py               # Script de gerenciamento Django
└── README.md              # Este arquivo
```

## Componentes Principais

### Modelos (`authentication/models.py`)

- **UserProfile**: Modelo de usuário estendido com configurações OTP
- **Geração de Código QR**: Criação automática de código QR TOTP
- **Gerenciamento de Dispositivos**: Integração com dispositivos django-otp

### Visualizações (`authentication/views.py`)

- **Registro**: Criação de conta de usuário com perfil
- **Autenticação**: Login com verificação OTP opcional
- **Configuração OTP**: Geração de código QR e confirmação de dispositivo
- **Verificação OTP**: Fluxo de autenticação de dois fatores
- **Visualizações Protegidas**: Conteúdo que requer verificação OTP

### Templates

- **Design Responsivo**: Interface Bootstrap amigável para dispositivos móveis
- **Estilo Moderno**: Fundos gradientes, animações, efeitos hover
- **Experiência do Usuário**: Instruções claras e feedback visual
- **Indicadores de Segurança**: Badges de status e dicas de segurança

## Guia de Uso

### 1. Registro de Usuário

1. Navegue até a página inicial
2. Clique em "Começar" ou "Registrar"
3. Preencha nome de usuário, email e senha
4. Envie o formulário para criar sua conta

### 2. Login Básico

1. Vá para a página de login
2. Digite seu nome de usuário e senha
3. Se OTP não estiver habilitado, você será logado diretamente

### 3. Configurando OTP

1. Do painel, clique em "Habilitar OTP"
2. Instale um aplicativo autenticador (Google Authenticator, Authy, etc.)
3. Escaneie o código QR ou digite manualmente a chave secreta
4. Digite o código de verificação de 6 dígitos
5. OTP está agora habilitado para sua conta

### 4. Login Protegido por OTP

1. Digite nome de usuário e senha como de costume
2. Você será redirecionado para verificação OTP
3. Abra seu aplicativo autenticador
4. Digite o código atual de 6 dígitos
5. Complete o login com autenticação de dois fatores

### 5. Acessando Conteúdo Seguro

1. Navegue para "Área Segura" do painel
2. Isso demonstra conteúdo protegido por OTP
3. Acessível apenas após verificação OTP

## Recursos de Segurança

### Proteção CSRF
- Todos os formulários incluem tokens CSRF
- Origens confiáveis configuradas para implantação

### Segurança de Sessão
- Gerenciamento seguro de sessão
- Rastreamento de estado de verificação OTP

### Segurança de Senha
- Validação de senha integrada do Django
- Hash seguro de senhas

### Segurança TOTP
- Rotação de token de 30 segundos
- Verificação baseada em tempo
- Confirmação de dispositivo necessária

## Compatibilidade com Aplicativo Autenticador

Esta implementação funciona com aplicativos autenticadores populares:

- **Google Authenticator** (iOS/Android)
- **Microsoft Authenticator** (iOS/Android)
- **Authy** (iOS/Android/Desktop)
- **1Password** (com suporte TOTP)
- **LastPass Authenticator**

## Endpoints da API

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Página inicial |
| `/register/` | GET/POST | Registro de usuário |
| `/login/` | GET/POST | Login de usuário |
| `/logout/` | GET | Logout de usuário |
| `/dashboard/` | GET | Painel do usuário |
| `/otp/setup/` | GET/POST | Configuração OTP |
| `/otp/verify/` | GET/POST | Verificação OTP |
| `/otp/disable/` | POST | Desabilitar OTP |
| `/secure/` | GET | Conteúdo protegido |

## Configuração

### Configurações Django

Configurações principais em `otp_project/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',  # Obrigatório para OTP
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Configuração CSRF

Para implantação, atualize `CSRF_TRUSTED_ORIGINS`:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://seudominio.com',
    'https://*.seudominio.com',
]
```

## Considerações de Implantação

### Configurações de Produção

1. **Modo Debug**: Defina `DEBUG = False`
2. **Chave Secreta**: Use variável de ambiente para `SECRET_KEY`
3. **Banco de Dados**: Configure banco de dados de produção (PostgreSQL recomendado)
4. **Arquivos Estáticos**: Configure servimento de arquivos estáticos
5. **HTTPS**: Garanta HTTPS para segurança

### Variáveis de Ambiente

```bash
export DJANGO_SECRET_KEY="sua-chave-secreta"
export DJANGO_DEBUG="False"
export DATABASE_URL="sua-url-do-banco"
```

## Solução de Problemas

### Problemas Comuns

1. **Falha na Verificação CSRF**
   - Verifique a configuração `CSRF_TRUSTED_ORIGINS`
   - Garanta que formulários incluam `{% csrf_token %}`

2. **Código OTP Inválido**
   - Verifique sincronização de tempo do dispositivo
   - Verifique se o código expirou (janela de 30 segundos)
   - Garanta entrada correta da chave secreta

3. **Código QR Não Exibindo**
   - Verifique instalação do `qrcode` e `Pillow`
   - Verifique permissões de geração de imagem

### Modo Debug

Habilite modo debug para desenvolvimento:

```python
DEBUG = True
```

## Melhores Práticas de Segurança

1. **Códigos de Backup**: Implemente códigos de backup para recuperação de conta
2. **Limitação de Taxa**: Adicione limitação de taxa para tentativas OTP
3. **Log de Auditoria**: Registre eventos de autenticação
4. **Timeout de Sessão**: Configure timeouts de sessão apropriados
5. **Apenas HTTPS**: Sempre use HTTPS em produção

## Contribuindo

Este é um projeto de demonstração. Para uso em produção:

1. Adicione tratamento abrangente de erros
2. Implemente métodos de autenticação de backup
3. Adicione limitação de taxa e proteção contra força bruta
4. Inclua log de auditoria
5. Adicione testes abrangentes

## Licença

Este projeto é fornecido como exemplo educacional. Use por sua conta e risco para aplicações de produção.

## Suporte

Para perguntas sobre django-otp, consulte a documentação oficial:
- [Documentação django-otp](https://django-otp.readthedocs.io/)
- [Documentação Django](https://docs.djangoproject.com/)

---

**Nota**: Esta é uma aplicação de demonstração. Para uso em produção, implemente medidas de segurança adicionais, tratamento de erros e testes.
