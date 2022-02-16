# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import datetime

class Fieles(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    assText = models.TextField('Asstext', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    date = models.DateField('Date',blank=True,default=datetime.datetime.now().date())

    # updated data fields
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('data_edit', kwargs={'pk': self.pk})
