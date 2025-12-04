from django.shortcuts import render,redirect
from authentication.models import UserModel
from django.contrib import messages
from .models import Product, Shop

def Dashboard(request):
    return render(request,'dashboard.html')
def Manager(request):
    users = UserModel.objects.all()
    context = {
        'users':users
    }
    return render(request,'manager.html',context)

def ManagerDelete(request,pk):
    user = UserModel.objects.get( id = pk)
    if request.method == "POST":
        if user.profile:
            user.profile.delete()
            user.delete()
            messages.success(request,'User Account Delete!')
            return redirect('/dashboard/manager/')
        
def AddManager(request):
    if request.method == "GET":
        return redirect(request,'manager.html')
    if request.method == "POST":
       username = request.POST['username']
       email = request.POST['email']
       profile = request.FILES.get('profile')
       position = request.POST['position']
       phone = request.POST['phone']
       password = request.POST['password']
       user = UserModel.objects.create(
           username = username,
           email  = email,
           profile = profile,
           position = position,
           phone = phone
       )
       user.set_password(password)
       user.save()
       messages.success(request,'Add User Successfully!')
       return redirect('/dashboard/manager/')
    
def ManagerUpdate(request,pk):
    user = UserModel.objects.get(id = pk)
    if request.method == "POST":
        user.username = request.POST['username']
        user.email = request.POST['email']
        if request.FILES.get('profile'):
            user.profile = request.FILES.get('profile')
        user.position = request.POST['position']
        user.phone = request.POST['phone']
        user.save()
        messages.success(request,'User Account Update!')
        return redirect('/dashboard/manager/')

def Daily_Sale(request):
    return render(request,'daily_sales.html')

def Daily_orders(request):
    return render(request,'daily_orders.html')


def Setting(request):
    return render(request,'setting.html')

def Request(request):
    return render(request,'request_table.html')

def Report(request):
    return render(request,'report.html')

def Settings(request):
     return render(request,'settings.html')

def SettingsUpdate(request,pk):
    user = UserModel.objects.get(id = pk)
    if request.method == 'POST':
            user.username = request.POST['username']
            user.position = request.POST['position']
            user.phone = request.POST['phone']
            user.email = request.POST['email']
            if request.FILES.get('profile'):
                user.profile = request.FILES.get('profile')
            user.save()
            messages.success(request,'Profile Update!')
            return redirect('/dashboard/settings/')
    context = {
        'user':user
    }
    return render(request,'settings.html',context)
   
##   product    ##
def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_upload(request):
    if request.method == "POST":
        Product.objects.create(
            code=request.POST["code"],
            name=request.POST["name"],
            price=request.POST["price"],
            photo=request.FILES["photo"]
        )
        return redirect("product_list")
def ShopUpload(request):
    shops = Shop.objects.all()
    context = {
        'shops':shops
    }
    return render(request,'shop.html',context)
def AddShop(request):
    if request.method == "GET":
        return render(request,'shop.html')
    if request.method == "POST":
        shops = Shop.objects.create(
            name = request.POST['name'],
            image = request.FILES.get('image'),
            phone = request.POST['phone'],
            address = request.POST['address'],
            remark = request.POST['remark']
        )
        shops.save()
        messages.success(request,'Add Shop Sucess!')
        return redirect('/dashboard/shop/')
def UpdateShop(request,pk):
    if request.method == "POST":
        shop = Shop.objects.get(id = pk)
        shop.name = request.POST['name']
        shop.phone = request.POST['phone']
        shop.address = request.POST['address']
        shop.remark = request.POST['remark']
        if request.FILES.get('image'):
            shop.image = request.FILES.get('image')
        shop.save()
        messages.success(request,'Shop Update Success!')
        return redirect('/dashboard/shop/')
def DeleteShop(request,pk):
    if request.method == "POST":
        shop = Shop.objects.get(id = pk)
        if shop.image:
            shop.image.delete()
            shop.delete()
            messages.success(request,'Shop Delete!')
            return redirect('/dashboard/shop/')

     
