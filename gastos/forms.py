# -*- coding: utf-8 -*-
from django import forms

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DataForm(forms.ModelForm):

    concepto_choices = (('combustible', 'Combustible'),('alimentos', 'Alimentos'),('hospedaje', 'Hospedaje'),('alimentos', 'Alimentos'),('peaje', 'Peaje'),('otros', 'Otros'))
    concepto = forms.ChoiceField(choices=concepto_choices)

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.fields['documento'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['concepto'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['monto'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['fecha'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        

    class Meta:

        model = Gastos

        fields = "__all__"

        widgets = {
            'fecha': DateInput(),
        }