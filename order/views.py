from django.shortcuts import redirect, render
from order.models import Basket,BasketItem
from django.views.generic import ListView, CreateView
from shop.forms import ProductForm
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models import Product


class BasketListView(ListView):
    template_name = "basket.html"    

    def get_queryset(self):
        open_basket = Basket.objects.filter(user_id=self.request.user.id, ordered=False).first()
        if open_basket:
            return open_basket.basketitems.all()
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['open_basket'] = Basket.objects.filter(user_id=self.request.user.id, ordered=False).first()
        return context




class BasketItemCreateView(LoginRequiredMixin,FormView):
    model = BasketItem
    form_class = ProductForm
    success_url =reverse_lazy('basket')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
 
        basket = Basket.objects.filter(user=self.request.user, ordered=False).first()
       
        if basket is None:
            basket = Basket.objects.create(user=self.request.user, ordered=False)
        product_id=form.cleaned_data.get('product_id')
        quantity = form.cleaned_data.get('quantity') 
        product_object = Product.objects.get(id=product_id)
        basketitem=basket.basketitems.filter(product_id=product_id)
        if basketitem.exists():
            basketitem.update(quantity=quantity)
        else:
            basket.basketitems.create(product_id=product_id, price=product_object.price, quantity=quantity)
        return super().form_valid(form)


    

