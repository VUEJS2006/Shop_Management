
from django.urls import path
from . import views
urlpatterns = [
   path('',views.Website,name='website'),
   path('orders/', views.Orders,name='orders'),
   path('sales/', views.Sales,name='sales')

]