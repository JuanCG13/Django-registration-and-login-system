# -*- coding: utf-8 -*-
from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.DataList.as_view()), name='fieles_list'),
    path('view/<int:pk>', login_required(views.DataDetail.as_view()), name='fieles_view'),
    path('new', login_required(views.DataCreate.as_view()), name='fieles_new'),
    path('edit/<int:pk>', login_required(views.DataUpdate.as_view()), name='fieles_edit'),
    path('delete/<int:pk>', login_required(views.DataDelete.as_view()), name='fieles_delete'),
]