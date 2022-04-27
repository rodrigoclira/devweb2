from django.contrib.auth.models import User

#Código de backend de autenticação simples que utiliza o email para validar o usuário

class EmailAuthBackend(object):
    """
    Faz a autenticação usando um endereço de e-mail
    """

    def authenticate(self, request, username=None, password=None):
        """
        Recebe o objeto request e as credenciais do usuário como parâmetro.
        Deve retornar um objeto user que corresponda a essas credenciais se
        elas forem válidas ou None caso contrário.
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None


    def get_user(self, user_id):
        """
        Aceita um id de usuário como parâmetro e deve devolver um objeto
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
