from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView

from .models import Autor,Libros


class Home(TemplateView):
    template_name="biblioteca/home.html"

class ListaAutores(ListView):
    template_name = "biblioteca/lista-autores.html"
    model = Autor
    context_object_name = 'autores'

class ListaLibros(ListView):
     """ Vista para listar todos los libros"""
     template_name = "biblioteca/lista-libros.html"
     model = Libros
     context_object_name = 'libros'

class ListaLibrosAutores(ListView):
     """ Vista para listar libros por autores"""
     template_name = "biblioteca/lista-libros.html"
     model = Libros
     context_object_name = 'libros'

     def get_queryset(self):
         #identificar el autor
         id = self.kwargs['pk']
         #filtro de los libros
         lista = Libros.objects.filter(autor=id)
         #devuelvo el resultado o la lista
         return lista

class AddAutor(CreateView):
    #Vista para registrar un nuevo autor
    template_name = 'biblioteca/add-autor.html'
    model = Autor
    #El fields lo que hace es referenciar los campos para el registro
    fields = ['nombre','nacionalidad']
    success_url = '/'