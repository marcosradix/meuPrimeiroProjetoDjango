from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')



def articles(request, year):
    return HttpResponse('O ano enviado foi: {} '.format(str(year)))


def ler_do_banco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'João', 'idade': 27}
    ]
    for pessoa in lista_nomes:
        if (pessoa['nome'] == nome):
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}


def fname(request, nome):
    result = ler_do_banco(nome)
    if(result['idade'] > 0):
        return HttpResponse('Pessoa encontrada com ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('Pessoa não encontrada')


def fname2(request, nome):
    idade = ler_do_banco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})















