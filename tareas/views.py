from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarea


# Create your views here.

def lista_tareas(request):
    pendientes = Tarea.objects.filter(hecha=False).order_by("creada")
    completadas = Tarea.objects.filter(hecha=True).order_by("creada")
    return render(request, "tareas/lista.html", {
        "pendientes": pendientes,
        "completadas": completadas, 
    })

@require_POST
def agregar_tarea(request):
    texto = request.POST.get("texto", "").strip()
    if texto:
        Tarea.objects.create(texto=texto)
    return redirect("lista")

@require_POST
def alternar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.hecha = not tarea.hecha
    tarea.save()
    return redirect("lista")

@require_POST
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect("lista")

@require_POST
def limpiar_completadas(request):
    Tarea.objects.filter(hecha=True).delete()
    return redirect("lista")
