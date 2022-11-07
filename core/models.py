from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self. name 
    

# class Total_in_storeModel(models.Model):
#     category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
#     Rqty= models.OneToOneField(CategoryModel, on_delete=models.CASCADE)
#     re_qty=models.IntegerField(null=True,blank=True)    
    
class StoreModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    in_day = models.DateField(auto_now_add=True)
    qty = models.IntegerField()
    re_q= models.IntegerField(null=True, blank=True)
    
    
    
    # def __str__(self):
    #     return f"we have {self.qty} of {self.category} is store"
    

class SaleModel(models.Model):
    category= models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True) 
    qty = models.IntegerField()
    sale_price= models.DecimalField(max_digits=5, decimal_places=2)
    total = models.IntegerField(null=True, blank=True)   
    
    def __str__(self):
        return f"Costumer your bill of {self.category} qty _{self.qty} price of one {self.sale_price} Total {self.total} "