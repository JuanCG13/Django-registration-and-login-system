# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from gastos.models import *
from entrada.models import *
from diezmo.models import *

@login_required
def informes_view(request):

    gasto_total = Gastos.objects.aggregate(Sum('monto'))
    gasto_total = gasto_total['monto__sum']

    if not gasto_total:
        gasto_total = 0

    entrada_total = Entrada.objects.aggregate(Sum('monto'))
    entrada_total = entrada_total['monto__sum']

    if not entrada_total:
        entrada_total = 0

    diezmo_total = Diezmo.objects.aggregate(Sum('monto'))
    diezmo_total = diezmo_total['monto__sum']

    if not diezmo_total:
        diezmo_total = 0

    ingreso_total = entrada_total + diezmo_total
    ingreso_neto = ingreso_total - gasto_total

    # print(entrada_total['monto__sum'])
    # print(diezmo_total['monto__sum'])
    # print(gasto_total['monto__sum'])
    # print(ingreso_total)
    # print(ingreso_neto)
    return render(request,'informes/informes_detail.html',{
        'ingreso_total':ingreso_total,
        'gasto_total':gasto_total,
        'ingreso_neto':ingreso_neto,
    })




