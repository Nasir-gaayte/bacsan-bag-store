from django.shortcuts import render, redirect
from .models import CategoryModel, SaleModel, StoreModel


# Create your views here.


def home(request):
    cat = CategoryModel.objects.all()
    st = StoreModel.objects.all()
    sales = SaleModel.objects.all()
    
    return render(request,'core/home.html',{
        'cat':cat,
        'st':st,
        'sales':sales,
        })