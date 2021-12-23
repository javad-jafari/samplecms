from django.contrib import admin
from django.urls import path,include
from shop.views import  ProductListView, ProductDetailView, ProductByCategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<uuid:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('category/<uuid:pk>', ProductByCategoryListView.as_view(), name='product-by-category'),
]
