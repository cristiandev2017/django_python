from django.urls import path, re_path

from . import views

app_name="biblioteca_app"

urlpatterns = [
    path('', views.Home.as_view(),name="home"),
    path('autores', views.ListaAutores.as_view(),name="lista-autores"),
    path('libros/todos', views.ListaLibros.as_view(),name="lista-libros-todos"),
    path('libros-autor/<pk>/por-autor/', views.ListaLibrosAutores.as_view(),name="lista-libros"),
    path('autor/add/', views.AddAutor.as_view(),name="autor-add")
]