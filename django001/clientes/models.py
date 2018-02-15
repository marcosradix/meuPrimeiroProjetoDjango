from django.db import models

# Create your models here.
#admin123456 senha do admin
from django.db import models

class Person(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.primeiro_nome