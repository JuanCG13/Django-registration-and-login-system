# -*- coding: utf-8 -*-
from django import forms

from .models import Product

class DateInput(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):

    input_choices = (('option 1', 'option 1'),('option 3', 'option 2'),('option 4', 'option 4'))
    name = forms.ChoiceField(choices=input_choices)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['assText'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['date'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:

        model = Product

        fields = "__all__"

        widgets = {
            'date': DateInput(),
        }