
from django.urls import path
from . import views
urlpatterns = [
   path('dashboard/',views.Dashboard, name='dashboard'),
   path('manager/',views.Manager, name='manager'),
   path('sale/',views.AdminSale, name='admin_sale'),
   path('shop/',views.Shop, name='shop'),
]
