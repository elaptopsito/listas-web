from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['texto']
        labels = {'texto': 'Texto de la tarea'}