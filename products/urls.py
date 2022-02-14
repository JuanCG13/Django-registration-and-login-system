# -*- coding: utf-8 -*-
from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.ProductList.as_view()), name='product_list'),
    path('view/<int:pk>', login_required(views.ProductDetail.as_view()), name='product_view'),
    path('new', login_required(views.ProductCreate.as_view()), name='product_new'),
    path('edit/<int:pk>', login_required(views.ProductUpdate.as_view()), name='product_edit'),
    path('delete/<int:pk>', login_required(views.ProductDelete.as_view()), name='product_delete'),
]