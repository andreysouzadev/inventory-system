# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm
# from .models import UserProfile

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # Cria o usuário na tabela User do Django
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )
#             # Salva os outros dados no modelo UserProfile
#             register_user = UserProfile(
#                 user=user,
#                 nome_completo=form.cleaned_data['nome_completo'],  # Nome completo
#                 telefone=form.cleaned_data['telefone'],
#                 funcao=form.cleaned_data['funcao'],
#             )
#             register_user.save()

#             print("Usuário cadastrado com sucesso")
#             messages.success(request, 'Cadastro realizado com sucesso!')
#             return redirect('login')
#         else:
#             print("Usuário não cadastrado")
#             messages.error(request, 'Cadastro não realizado. Corrija os erros abaixo.')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register.html', {'form': form})


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm
# from .models import UserProfile

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # Cria o usuário na tabela User do Django
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )
#             # Salva os outros dados no modelo UserProfile
#             register_user = UserProfile(
#                 user=user,
#                 nome_completo=form.cleaned_data['nome_completo'],
#                 telefone=form.cleaned_data['telefone'],
#                 funcao=form.cleaned_data['funcao'],
#             )
#             register_user.save()

#             messages.success(request, 'Cadastro realizado com sucesso!')
#             return redirect('login')
#         else:
#             # Adiciona as mensagens de erro ao sistema de mensagens do Django
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, error)

#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register.html', {'form': form})

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm
# from .models import UserProfile

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )
#             register_user = UserProfile(
#                 user=user,
#                 telefone=form.cleaned_data['telefone'],
#                 funcao=form.cleaned_data['funcao'],
#             )
#             register_user.save()

#             messages.success(request, 'Cadastro realizado com sucesso!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Usuário não cadastrado, revise todos os campos.')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register.html', {'form': form})

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
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
        else:
            # Adiciona mensagem geral de erro
            messages.error(request, 'Usuário não cadastrado, revise todos os campos.')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



