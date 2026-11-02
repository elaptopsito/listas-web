from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tareas, name="lista"),
    path("agregar/", views.agregar_tarea, name="agregar"),
    path("alternar/<int:pk>/", views.alternar_tarea, name="alternar"),
    path("eliminar/<int:pk>/", views.eliminar_tarea, name="eliminar"),
    path("limpiar/", views.limpiar_completadas, name="limpiar"),
    path("editar/<int:pk>/", views.editar_tarea, name="editar"),
]