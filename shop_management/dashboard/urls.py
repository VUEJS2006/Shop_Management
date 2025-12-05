
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
   path('setting/',views.Setting, name='setting'),
   path('daily_orders/',views.Daily_orders, name='daily_orders'),
   path('request_table/',views.Request, name='request'),
   path('report/',views.Report, name='report'),
   # Products
   path("products/", views.product_list, name="product_list"),
   path('products/delete/<int:pk>',views.DeleteProduct, name='delete_product'),
   path("products/upload/", views.product_upload, name="product_upload"),
   path('products/update/<int:pk>',views.UpdateProduct, name='update_product'),
   # settings
   path('settings/',views.Settings, name='settings'),
   path('settings/update/<uuid:pk>',views.SettingsUpdate, name='setting_update'),
   # shop 
   path('shop/',views.ShopUpload, name='shop'),
   path('shop/create/',views.AddShop, name='add_shop'),
   path('shop/update/<int:pk>',views.UpdateShop, name='update_shop'),
   path('shop/delete/<int:pk>',views.DeleteShop, name='delete_shop'),
 
  

]
