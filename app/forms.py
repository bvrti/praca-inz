from django import forms
from django.forms import ModelForm
from .models import malfunction

class reportMalfunctionForm(ModelForm):

    class Meta :
        model = malfunction
        fields = ['machine_name', 'description']
        widgets = {
            'machine_name': forms.TextInput(attrs={'placeholder': 'Nazwa maszyny:'}),
            'description': forms.Textarea(attrs={'placeholder': 'Opis:'}),
        }
        labels = {
            'machine_name': '',
            'description': '',
        }