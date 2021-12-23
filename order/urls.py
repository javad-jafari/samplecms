
from django.urls import path,include
from order.views import OrdertView


urlpatterns = [
    path('basket',OrdertView.as_view(), name='basket' )
    ]