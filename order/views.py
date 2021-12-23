from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


class OrdertView(TemplateView):
    template_name = "basket.html"
