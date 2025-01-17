from urllib import request
from django.db.models import Count
from django.http import Http404, HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerProfileForm
from .forms import PaymentForm
import razorpay
from .models import Product,Customer,Cart,Payment
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def index(request):
    return render(request,'index.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')#.annotate(total=Count('title'))
        return render(request,'category.html',locals())

class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'productdetails.html',locals())

def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id').strip('/')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.selling_price
        amount = amount + value
    totalamount = amount + 200
    return render(request,'addtocart.html',locals())

def plus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 200
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount' :totalamount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 200
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount' :totalamount,
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 200
        # print(prod_id)
        data={
           
            'amount':amount,
            'totalamount' :totalamount,
        }
        return JsonResponse(data)

def payment(request):
    if request.method == "POST":
        
        user =request.POST.get("user")
        amount = int(request.POST.get('amount'))
        client = razorpay.Client(auth =('rzp_test_CcTEsYTF0zU1hl','JUFpc9VKem4BmOwVOUbsafu7'))
        pay = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
        print(pay)
        payment_data = Payment(user,amount=amount,order_id=pay['id'])
        return render(request,"pay.html",{'payment':payment_data})
    form = PaymentForm()
    return render(request, "pay.html", {"form": form, "payment": payment})

def success(request):
    if request.method == 'POST':
        a= request.POST
        print(a)
    return render(request ,'success.html')

        
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm
        return render(request,'profile.html',locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            # name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            pincode=form.cleaned_data['pincode']

            reg= Customer(user=user,locality=locality,city=city,mobile=mobile,pincode=pincode)
            reg.save()
            messages.success(request,'profile save successfully')
        return render(request,'profile.html',locals())

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())



def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def user(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('user')
        if User.objects.filter(email = email).first():
            messages.error(request,"Email already taken")
            return redirect('user')

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('user')

        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.name = name
        myuser.save()
        messages.success(request,"Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request,'reg.html')
    
def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in!")
            return redirect('index')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('user')

    else:
        print("error")
        return render(request,'login.html')

def signout(request):
        logout(request)
        messages.success(request,"Successfully logged out!")
        return redirect('user')
