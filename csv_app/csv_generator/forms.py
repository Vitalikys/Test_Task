from django import forms

from .models import Schema


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = 'name', 'separator', 'string_character', 'full_name', 'age', 'job'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'separator': forms.Select(attrs={'class': 'form-select'}),
            'string_character': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'})
        }



