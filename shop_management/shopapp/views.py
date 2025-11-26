from django.shortcuts import render

def Website(request):
    return render(request,'website.html')

def Orders(request):
    return render(request,'orders.html')

def Sales(request):
    return render(request, 'sales.html')
