from django.contrib.auth.models import User

#Código de backend de autenticação simples que utiliza o email para validar o usuário

class EmailAuthBackend(object):
    """
    Faz a autenticação usando um endereço de e-mail
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

