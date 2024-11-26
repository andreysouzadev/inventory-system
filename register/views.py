from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            user_profile = UserProfile(
                user=user,
                telefone=form.cleaned_data['telefone'],
                nome_completo=form.cleaned_data['nome_completo'],
                funcao=form.cleaned_data['funcao'],
            )
            user_profile.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('login')
        else:
            # Adiciona mensagem geral de erro
            messages.error(request, 'Usuário não cadastrado, revise todos os campos.')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



