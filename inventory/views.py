from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from inventory.models import Categoria, Dispositivo

# Create your views here.

# test view
# def home(request):
#     # Dados de exemplo para cada categoria
#     notebooks = [{'nome': 'Notebook 1'}, {'nome': 'Notebook 2'}, {'nome': 'Notebook 3'}, {'nome': 'Notebook 3'}, {'nome': 'Notebook 3'}]
#     monitores = [{'nome': 'Monitor 1'}, {'nome': 'Monitor 2'}, {'nome': 'Monitor 3'}]
#     avayas = [{'nome': 'Avaya 1'}, {'nome': 'Avaya 2'}, {'nome': 'Avaya 3'}]

#     context = {
#         'notebooks': notebooks,
#         'monitores': monitores,
#         'avayas': avayas,
#     }
#     # return render(request, 'home.html')
#     return render(request, 'home.html', context)


# view model modal
# def home(request):
#     categorias = Categoria.objects.prefetch_related('dispositivos').all()
#     context = {'categorias': categorias}
#     return render(request, 'home.html', context)

def home(request):
    if request.method == "POST":
        nome_dispositivo = request.POST.get("device_name")
        categoria_id = request.POST.get("category")

        if nome_dispositivo and categoria_id:
            categoria  = Categoria.objects.get(id=categoria_id)
            Dispositivo.objects.create(nome=nome_dispositivo, categoria=categoria)
        return redirect("home")
    

    categorias = Categoria.objects.prefetch_related('dispositivos').all()
    context = {'categorias': categorias}
    return render(request, 'home.html', context)


#View para remover dispositivo.

def remover_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    dispositivo.delete()

    return redirect("home")
    



