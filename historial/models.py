# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import datetime

class Historial(models.Model):
    concepto = models.CharField('Concepto', max_length=100,blank=True)
    monto = models.DecimalField('Monto', decimal_places=2, max_digits=8,blank=True)
    fecha = models.DateField('Fecha',blank=True,default=datetime.datetime.now().date())

    # updated data fields
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['concepto']

    def __str__(self):
        return self.concepto + " - " + self.monto
        
    def get_absolute_url(self):
        return reverse('historial_edit', kwargs={'pk': self.pk})
