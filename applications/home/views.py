from django.shortcuts import render

from django.views.generic import TemplateView,ListView

class IndexView(TemplateView):
    #Una vista procesa los datos y renderiza los resultados en pantalla
    #Siempre pedira un template.(template = archivo html)
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['El quijote de la mancha','django volviendose bueno','aprendiendo con toda', 'le gano al fracaso']
    context_object_name = 'libros'