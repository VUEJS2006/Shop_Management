from django.shortcuts import render

def Dashboard(request):
    return render(request,'dashboard.html')
def Manager(request):
    return render(request,'manager.html')
def AdminSale(request):
    return render(request,'admin_sale.html')
def Shop(request):
    return render(request,'shop.html')