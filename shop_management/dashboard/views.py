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

def shop(request):
    shops = Shop.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        remark = request.POST.get("remark")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")
        if Shop.objects.filter(name=name).exists():
            return render(request, "shop.html", {
                "shops": shops,
                "error": "This shop name already exists!",
            })
        if Shop.objects.filter(phone=phone).exists():
            return render(request, "shop.html", {
                "shops": shops,
                "error": "This phone number already exists!",
            })
        shop = Shop.objects.create(
            name=name,
            phone=phone,
            remark=remark,
            address=address,
            photo=photo,
        )
        shop.save()
        messages.success(request,'Shop upload successfully!')
    return render(request, 'shop.html', {"shops": shops})

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
