from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from inventory.models import Categoria, Dispositivo

# Decorator para tratar acesso somente à usuários logados
@login_required(login_url='/login/')
def home(request):
    if request.method == "POST":
        nome_dispositivo = request.POST.get("device_name")
        categoria_id = request.POST.get("category")
        
        if nome_dispositivo and categoria_id:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                Dispositivo.objects.create(nome=nome_dispositivo, categoria=categoria)
            except Categoria.DoesNotExist:
                return HttpResponse("Categoria inválida", status=400)
        return redirect("home")


    categorias = Categoria.objects.prefetch_related('dispositivos').all()
    context = {'categorias': categorias}
    return render(request, 'home.html', context)


@login_required(login_url='/login/')
def remover_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    dispositivo.delete()
    return redirect("home")
