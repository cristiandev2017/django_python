from django.contrib import admin

from .models import Autor, Libros

#Clase para mejorar el administrador
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #aributo para buscar por un campo
    search_fields = ('nombre', 'nacionalidad',)

class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'autor',
        'id',
    )
    #aributo para buscar por un campo
    search_fields = ('nombre', 'nacionalidad',)
    #para poner filtros
    list_filter = ('autor',)

admin.site.register(Autor,AutorAdmin)
admin.site.register(Libros,LibrosAdmin)
