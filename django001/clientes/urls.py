
from django.urls import path
from .views import lista_pessoa

urlpatterns = [
    path('list/', lista_pessoa),

]
