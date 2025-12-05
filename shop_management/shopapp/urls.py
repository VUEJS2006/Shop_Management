
from django.urls import path
from . import views
urlpatterns = [
   path('orders/', views.Orders,name='orders'),
   path('sales/', views.Sales,name='sales'),
   path('home/', views.Home,name='home'),

]