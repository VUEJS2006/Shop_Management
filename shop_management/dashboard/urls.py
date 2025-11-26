
from django.urls import path
from . import views
urlpatterns = [
   path('dashboard/',views.Dashboard, name='dashboard'),
   path('manager/',views.Manager, name='manager'),
   path('daily_sale/',views.Daily_Sale, name='daily_sales'),
   path('shop/',views.Shop, name='shop'),
   path('setting/',views.Setting, name='setting'),
   path('daily_orders',views.Daily_orders, name='daily_orders'),
   path('request_table/',views.Request, name='request'),
   path('report',views.Report, name='report')
]
