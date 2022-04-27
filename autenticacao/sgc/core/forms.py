from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", 'first_name', 'email')

    # 'clean_nomedocampo' pode ser usado para limpar ou validar o formulário.
    # ele é automaticamente chamado pelo método 'clean' do MmodelForm
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords são diferentes")
        return cd['password2']
