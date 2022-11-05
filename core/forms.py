from django import forms
from .models import SaleModel



class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleModel
        fields = ("category", "sale_price", "qty")