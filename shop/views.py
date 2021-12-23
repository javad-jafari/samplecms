from django.db import models
from django.db.models import query
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Product, Category
from shop.forms import ProductForm
from django.shortcuts import get_object_or_404



class ProductListView(ListView):
    model = Product
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['features_car_1'] = Product.objects.all()[0]
        context['features_car_2'] = Product.objects.all()[1]
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('pk')
        context['form'] = ProductForm(initial={'product_id':product_id})
        return context


class ProductByCategoryListView(ListView):
    template_name = "category.html"
 
    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category_id=self.kwargs['pk'])
