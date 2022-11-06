from django import forms
from .models import SaleModel, CategoryModel, StoreModel



class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleModel
        fields = ("category", "sale_price", "qty")
        
        
        
class Categoryform(forms.ModelForm):
    class Meta:
        model =  CategoryModel
        fields = ("name", "price")       
        
        
class Storeform(forms.ModelForm):
    class Meta:
        model =  StoreModel
        fields = ("category","qty")               