from django.shortcuts import render

def Dashboard(request):
    return render(request,'dashboard.html')
def Manager(request):
    return render(request,'manager.html')
def Daily_Sale(request):
    return render(request,'daily_sales.html')

def Daily_orders(request):
    return render(request,'daily_orders.html')
def Shop(request):
    return render(request,'shop.html')
def Setting(request):
    return render(request,'setting.html')

def Request(request):
    return render(request,'request_table.html')

def Report(request):
    return render(request,'report.html')