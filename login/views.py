from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print("Username:", username)  
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('home')
        else:
            print("Usuário não autenticado.")
            messages.error(request, 'Login ou senha inválidos. Verifique e tente novamente')
    
    return render(request, 'login.html')

