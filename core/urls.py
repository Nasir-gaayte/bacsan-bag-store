from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('dailly/',views.add_sale,name='dailly'),
    path('add_cat/',views.add_cat,name='add_cat'),
    path('add_product/',views.add_product,name='add_product'),
]
