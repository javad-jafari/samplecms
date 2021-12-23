
from django.urls import path,include
from order.views import BasketListView, BasketItemCreateView



urlpatterns = [
    path('basket',BasketListView.as_view(), name='basket' ),
    path('addtobasket',BasketItemCreateView.as_view(), name='addtobasket' )
    ]