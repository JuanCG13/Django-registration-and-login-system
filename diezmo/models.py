# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import datetime


class Diezmo(models.Model):
    monto = models.DecimalField('Monto', decimal_places=2, max_digits=128,blank=True)
    fecha = models.DateField('Fecha',blank=True,default=datetime.datetime.now().date())
    fecha_anio_mes = models.DateField('Año-Mes Correspondiente',blank=True,default=datetime.datetime.now().date())

    # updated data fields
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    # foreign key

    fiel_id = models.ForeignKey('fieles.Fieles',on_delete=models.CASCADE,null=True)


    class Meta:
        ordering = ['monto']

    def __str__(self):
        return str(self.fiel_id) + ' ' + str(self.monto)
        
    def get_absolute_url(self):
        return reverse('data_edit', kwargs={'pk': self.pk})
