# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Diezmo as model_data
from .forms import *

from historial.models import *

class DataList(ListView): 
    model = model_data

class DataDetail(DetailView): 
    model = model_data

class DataCreate(SuccessMessageMixin, CreateView): 
    model = model_data
    form_class = DataForm
    success_url = reverse_lazy('data_list')
    success_message = "Registro creado correctamente!"

    # code for log create model 
    def form_valid(self, form):

        current_user = self.request.user

        save_historial = Historial(usuario="{}".format(current_user.username),accion="Se ha agregado un diezmo")
        save_historial.save()

        return super().form_valid(form)

class DataUpdate(SuccessMessageMixin, UpdateView): 
    model = model_data
    form_class = DataForm
    success_url = reverse_lazy('data_list')
    success_message = "Registro actualizado correctamente"

    # code for log update model 
    def form_valid(self, form):

        current_user = self.request.user

        save_historial = Historial(usuario="{}".format(current_user.username),accion="Se ha actualizado un diezmo")
        save_historial.save()

        return super().form_valid(form)

class DataDelete(SuccessMessageMixin, DeleteView):
    model = model_data
    success_url = reverse_lazy('data_list')
    success_message = "Registro eliminado correctamente!"

    # code for log delete model 
    def get_queryset(self):

        query_set = super(DataDelete, self).get_queryset()

        if self.request.method == 'POST':

            current_user = self.request.user

            save_historial = Historial(usuario="{}".format(current_user.username),accion="Se ha eliminado un diezmo")
            save_historial.save()

        return query_set


