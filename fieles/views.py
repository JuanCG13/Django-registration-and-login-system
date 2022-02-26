# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Fieles as model_data
from .forms import *

class DataList(ListView): 
    model = model_data

class DataDetail(DetailView): 
    model = model_data

class DataCreate(SuccessMessageMixin, CreateView): 
    model = model_data
    form_class = DataForm
    success_url = reverse_lazy('fieles_list')
    success_message = "Registro creado correctamente!"

class DataUpdate(SuccessMessageMixin, UpdateView): 
    model = model_data
    form_class = DataForm
    success_url = reverse_lazy('fieles_list')
    success_message = "Registro actualizado correctamente"

class DataDelete(SuccessMessageMixin, DeleteView):
    model = model_data
    success_url = reverse_lazy('fieles_list')
    success_message = "Registro eliminado correctamente!"


