from django.contrib import admin
from .models import CategoryModel, StoreModel, SaleModel
# Register your models here.


admin.site.register(CategoryModel)
admin.site.register(StoreModel)
admin.site.register(SaleModel)

