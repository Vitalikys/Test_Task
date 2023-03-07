from django import forms

from .models import Schema, Column, DataSet


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = 'name', 'separator', 'string_character'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'separator': forms.Select(attrs={'class': 'form-select'}),
            'string_character': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'integer_num': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'})
        }


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('full_name', 'integer_num', 'job', 'email', 'domain_name',
                  'phone_number', 'company', 'text', 'address', 'date_fake',
                  'min_value_int', 'max_value_int')
        # exclude = ( )


class RowsForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ('rows', )
        widgets = {
            'rows': forms.NumberInput(attrs={'class': 'form-control',
                                           "placeholder": "number rows"}),
        }
