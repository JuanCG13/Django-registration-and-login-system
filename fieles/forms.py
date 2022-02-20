# -*- coding: utf-8 -*-
from django import forms

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DataForm(forms.ModelForm):

    sexo_choices = (('masculino', 'Masculino'),('femenino', 'Femenino'))
    sexo = forms.ChoiceField(choices=sexo_choices)

    estado_civil_choices = (('soltero', 'Soltero'),('casado', 'Casado/a'),('divorciado', 'Divorciado/a'),('viudo', 'Viudo/a'),('union_libre', 'Union Libre'))
    estado_civil = forms.ChoiceField(choices=estado_civil_choices)

    ciudad_choices = (('san_ignacio', 'San Ignacio'),('santa_rosa', 'Santa Rosa'),('san_juan', 'San Juan'),('ayolas', 'Ayolas'),('santa_maria', 'Santa Maria'))
    ciudad = forms.ChoiceField(choices=ciudad_choices)

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['apellido'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['sexo'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['edad'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['estado_civil'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['cedula'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['telefono'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['barrio'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['referencia'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['fecha'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['ciudad'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        

    class Meta:

        model = Fieles

        fields = "__all__"

        widgets = {
            'fecha': DateInput(),
        }