from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.

def registrar(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            novo_user = user_form.save(commit=False)
            novo_user.set_password(user_form.cleaned_data['password'])
            novo_user.save()
            return render(request, 'core/registro_realizado.html', {'novo_user': novo_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'core/registro.html',  {'user_form': user_form})
