from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Tarea
from .forms import TareaForm, RegistroForm
from django.contrib.auth import login


# Create your views here.

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("lista")
    else:
        form = RegistroForm()
    return render(request, "registration/registro.html", {"form": form})


@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    pendientes = tareas.filter(hecha=False).order_by("creada")
    completadas = tareas.filter(hecha=True).order_by("creada")
    return render(request, "tareas/lista.html", {
        "pendientes": pendientes,
        "completadas": completadas, 
    })

@login_required
@require_POST
def agregar_tarea(request):
    texto = request.POST.get("texto", "").strip()
    if texto:
        Tarea.objects.create(usuario=request.user, texto=texto)
    return redirect("lista")

@login_required
@require_POST
def alternar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    tarea.hecha = not tarea.hecha
    tarea.save()
    return redirect("lista")

@login_required
@require_POST
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    tarea.delete()
    return redirect("lista")

@login_required
@require_POST
def limpiar_completadas(request):
    Tarea.objects.filter(hecha=True, usuario=request.user).delete()
    return redirect("lista")

@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = TareaForm(instance=tarea)
    return render(request, "tareas/editar.html", {"form": form, "tarea": tarea})