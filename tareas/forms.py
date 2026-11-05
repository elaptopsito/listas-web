from django import forms
from .models import Tarea
from django.contrib.auth.forms import UserCreationForm

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['texto']
        labels = {'texto': 'Texto de la tarea'}

class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username"]
        