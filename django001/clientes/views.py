from django.shortcuts import render

# Create your views here.
def lista_pessoa(request):
    return render(request, 'pessoa.html')