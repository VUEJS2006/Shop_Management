from django.shortcuts import render

def Orders(request):
    return render(request,'orders.html')

def Sales(request):
    return render(request, 'sales.html')
