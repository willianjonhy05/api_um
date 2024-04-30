from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import LivroSerializer, AutorSerializer
# Create your views here.

def home(request):
    template_name = 'home.html'
    livros = Livro.objects.all()
    autores = Autor.objects.all()
    context = {
        'livros': livros,
        'autores': autores,
    }
    return render(request, template_name, context)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('-nome')
    serializer_class = AutorSerializer
    

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all().order_by('-titulo')
    serializer_class = LivroSerializer
    


