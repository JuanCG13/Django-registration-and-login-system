# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import datetime

class Fieles(models.Model):
    nombre = models.CharField('Name', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    sexo = models.CharField('Sexo', max_length=100)
    edad = models.CharField('Edad', max_length=100)
    estado_civil = models.CharField('Estado Civil', max_length=100)
    cedula = models.CharField('Cedula', max_length=100)
    telefono = models.CharField('Telefono', max_length=100)
    email = models.CharField('Email', max_length=100)
    barrio = models.TextField('Barrio', blank=True)
    referencia = models.TextField('Referencia', blank=True)
    fecha = models.DateField('Fecha de Nacimiento',blank=True,default=datetime.datetime.now().date())
    ciudad = models.CharField('Ciudad', max_length=100)

    # updated data fields
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
        
    def get_absolute_url(self):
        return reverse('fieles_edit', kwargs={'pk': self.pk})
