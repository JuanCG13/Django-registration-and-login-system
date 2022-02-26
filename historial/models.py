# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import datetime

class Historial(models.Model):
    usuario = models.CharField('Usuario', max_length=100,blank=True)
    accion = models.CharField('Accion', max_length=100,blank=True)

    # updated data fields
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['usuario']

    def __str__(self):
        return self.usuario + " - " + self.accion
        
    def get_absolute_url(self):
        return reverse('historial_edit', kwargs={'pk': self.pk})
