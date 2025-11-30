
from django.urls import path
from . import views
urlpatterns = [
   path('dashboard/',views.Dashboard, name='dashboard'),
   # Manager
   path('manager/',views.Manager, name='manager'),
   path('manager/delete/<uuid:pk>',views.ManagerDelete, name='manager_delete'),
   path('manager/create/',views.AddManager, name='manager_create'),
   path('manager/update?/<uuid:pk>',views.ManagerUpdate,name='manager_update'),
   path('daily_sale/',views.Daily_Sale, name='daily_sales'),
   path('shop/',views.Shop, name='shop'),
   path('setting/',views.Setting, name='setting'),
   path('daily_orders/',views.Daily_orders, name='daily_orders'),
   path('request_table/',views.Request, name='request'),
   path('report/',views.Report, name='report'),
   path("products/", views.product_list, name="product_list"),
   path("products/upload/", views.product_upload, name="product_upload"),
   path('settings/',views.Settings, name='settings'),
   path('settings/update/<uuid:pk>',views.SettingsUpdate, name='setting_update'),
]
