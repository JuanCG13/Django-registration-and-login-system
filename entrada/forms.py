# -*- coding: utf-8 -*-
from django import forms

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DataForm(forms.ModelForm):

    concepto_choices = (('servicio_central', 'Servicio Central'),('servicio_juvenil', 'Servicio Juvenil'),('casas_de_paz', 'Casas de Paz'))
    concepto = forms.ChoiceField(choices=concepto_choices)

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)

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

        model = Entrada

        fields = "__all__"

        widgets = {
            'fecha': DateInput(),
        }