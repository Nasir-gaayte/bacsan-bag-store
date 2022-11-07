from django.shortcuts import render, redirect
from .models import CategoryModel, SaleModel, StoreModel
from .forms import SaleForm, Storeform, Categoryform
import math
# Create your views here.


def home(request):
    cat = CategoryModel.objects.all()
    st = StoreModel.objects.all()
    sales = SaleModel.objects.all()
    
    
  
    
    # for x in toget:
    #     for y in toget2:
    #         xxx = ''
    #         xx = int(x.qty-y.qty)
    #         xxx = xx
    #         print(xxx)
    #         x.save()
            
    
    
    for x in st:   
        for y in sales:
            if x.category == y.category:   
                if x.re_q == 0:
                     
                        total = int(x.qty-y.qty)    
                        x.re_q = total
                        x.save()
                elif x.re_q:
                   
                        total = int(x.re_q-y.qty) 
                        print(total)
                        x.re_q = total
                        x.save()   
                        print(total)
                        
                else:
                    x.save()        
                print(x.re_q)
                print(y)
                
                
      
       
     
   
         
    for s in sales:
        s.total = ''
        totalss = float(s.qty*s.sale_price)
        s.total=totalss
        s.save()
        
        
        
    # for co in sales:
    #     ss =sum(float(co.total))
    #     print(ss)
        
    all_sale = SaleModel.objects.all()
    total_sales= sum(float(co.total) for co in all_sale)
        
    
        # ssss = math.fsum(sss)    
        # print(ssss)
       
    
       
            
           
        # to_sa = math.fsum(ss)
        # print(to_sa)
        
        
        
        
        # for u in ss:
        #     to_sa = sum(u)
        #     print(to_sa)
        
        

    
    
    
    return render(request,'core/home.html',{
        'cat':cat,
        'st':st,
        'sales':sales,
        'total_sales':total_sales,
        
        })
    
    
def add_sale(request):
    if request.method == "POST":
        form= SaleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = SaleForm()
    return  render(request,'core/dailly.html',{'form':form})      



def add_cat(request):
    if request.method == "POST":
        form = Categoryform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Categoryform()
    return render(request,'core/add_cat.html',{'form':form})    


def add_product(request):
    if request.method == "POST":
        form= Storeform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    form= Storeform()
    return render(request,'core/add_product.html',{'form':form})    