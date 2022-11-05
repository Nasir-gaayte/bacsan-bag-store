from django.shortcuts import render, redirect
from .models import CategoryModel, SaleModel, StoreModel
from .forms import SaleForm

# Create your views here.


def home(request):
    cat = CategoryModel.objects.all()
    st = StoreModel.objects.all()
    sales = SaleModel.objects.all()
    
    
    for x in st:
        for y in sales:
            x.re_q= ''
            total = int(x.qty-y.qty)
            x.re_q = total
            x.save()
            
      
        print(total)  
     
   
         
    for s in sales:
        s.total = ''
        total = float(s.qty*s.sale_price)
        s.total=total
        s.save()
    
    
    
    return render(request,'core/home.html',{
        'cat':cat,
        'st':st,
        'sales':sales,
        })
    
    
def add_sale(request):
    if request.method == "POST":
        form= SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = SaleForm()
    return  render(request,'core/dailly.html',{'form':form})      