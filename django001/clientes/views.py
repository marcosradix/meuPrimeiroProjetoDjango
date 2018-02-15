from django.shortcuts import render
from .models import Person
# Create your views here.
def lista_pessoa(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'objectPerson': persons})