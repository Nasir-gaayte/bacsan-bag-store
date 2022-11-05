from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('dailly/',views.add_sale,name='dailly'),
]
