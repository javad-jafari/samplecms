from django import forms


class ProductForm(forms.Form):
    product_id = forms.CharField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(widget=forms.NumberInput(), initial=1)
    