from django.shortcuts import render,redirect
from authentication.models import UserModel
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
def LoginView(request):
    if request.method == "GET":  
   #   if request.user.is_superuser:
   #      return redirect('/dashboard/dashboard/')
     return render(request,'login.html')
    if request.method == "POST":
       email = request.POST['email']
       password = request.POST['password']
       user = authenticate(
          email = email,
          password = password
       )
       if user is not None:
          login(request,user)
          if request.user.is_superuser:
             return redirect('/dashboard/dashboard/')
          else:
            return redirect('/website/sales/')
       else:
          messages.error(request,'Email or Password Not Found!')
          return redirect('/')
def RegisterView(request):
    if request.method == "GET":
     return render(request,'register.html')
    if request.method == "POST":
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       con_password = request.POST['con_password']
       profile = request.FILES['profile']
       position = request.POST['position']
       phone = request.POST['phone']
       if UserModel.objects.filter(email = email):
          messages.error(request,'Your Email Already Exists!')
          return redirect('/register/')
       if UserModel.objects.filter(username = username):
          messages.error(request,'Your Username Already Exists!')
          return redirect('/register/')
       if UserModel.objects.filter(phone = phone):
          messages.error(request,'Your Phone Already Exists!')
          return redirect('/register/')
       if password == con_password:
          user = UserModel.objects.create_user(
             username = username,
             email = email,
             password = password,
             profile = profile,
             position = position,
             phone = phone
          )
          user.save()
          messages.success(request,'Your Account Create Succcessfully!')
          return redirect('/')
       else:
          messages.error(request,'Your Email or Password or Phone is wrong!')
          return redirect('/register/')
def LogoutView(request):
   logout(request)
   return redirect('/')
          

