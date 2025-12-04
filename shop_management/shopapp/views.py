from django.shortcuts import render
from dashboard.models import Product
def Orders(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'orders.html',context)

def Sales(request):
    return render(request, 'sales.html')
