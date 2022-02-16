# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Fieles 
from .forms import *

class DataList(ListView): 
    model = Fieles

class DataDetail(DetailView): 
    model = Fieles

class DataCreate(SuccessMessageMixin, CreateView): 
    model = Fieles
    form_class = DataForm
    success_url = reverse_lazy('fieles_list')
    success_message = "Data successfully created!"

class DataUpdate(SuccessMessageMixin, UpdateView): 
    model = Fieles
    form_class = DataForm
    success_url = reverse_lazy('fieles_list')
    success_message = "Data successfully updated!"

class DataDelete(SuccessMessageMixin, DeleteView):
    model = Fieles
    success_url = reverse_lazy('fieles_list')
    success_message = "Data successfully deleted!"


