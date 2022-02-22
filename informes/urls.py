# -*- coding: utf-8 -*-
from django.urls import path
from .views import *



urlpatterns = [
    path('', informes_view, name='informes_view')
]