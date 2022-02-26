# -*- coding: utf-8 -*-
from django import forms

from .models import *

from fieles.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DataForm(forms.ModelForm):

    fiel_id = forms.ModelChoiceField(queryset=Fieles.objects.all(), to_field_name="id")

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)

        self.fields['monto'].widget.attrs = {
            'class': 'form-control col-md-6',
            'required':'required'
        }
        self.fields['fiel_id'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['fecha'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['fecha_anio_mes'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        

    class Meta:

        model = Diezmo

        fields = "__all__"

        widgets = {
            'fecha': DateInput(),
            'fecha_anio_mes': DateInput(),
        }