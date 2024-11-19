from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Log para depuração
        print("Username:", username)  
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            print("Login efetuado com sucesso")
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Verifique e tente novamente.')
    
    return render(request, 'login.html')


