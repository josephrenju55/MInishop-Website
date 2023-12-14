from django.http import HttpResponse
from home.models import *
from . models import *
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.session.create()
    return ct_id

@login_required(login_url='register')  # login url for when user is not authenticated
def add_cart(request,product_id):
    prod=shop.objects.get(id=product_id)
    user = request.user

    try:
        ct=cartlist.objects.get(user=user)
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request),user=user)
        ct.save()

    try:
        c_items=cartitems.objects.get(product=prod,cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
            prod.stock -=1
            prod.save()
        c_items.save()
    except cartitems.DoesNotExist:
        c_items=cartitems.objects.create(product=prod,quantity=1,cart=ct)
        prod.stock -=1
        prod.save()
        c_items.save()
    return redirect('cart')

def cart(request,tot=0,count=0,cart_items=None,ct_items=None):
    try:
        user=request.user

        if user.is_authenticated:
            ct = cartlist.objects.filter(user=user)

        else:
            cart_id = request.session.get('cart_id')
            ct = cartlist.objects.filter(cart_id=cart_id)

        ct_items = cartitems.objects.filter(cart__in=ct, available=True)
        for i in ct_items:
            tot += (i.product.price * i.quantity)
            count += i.quantity

    except ObjectDoesNotExist:
        return HttpResponse("<script> alert('Empty Cart');window.locations='/';</script>")
    
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})


@login_required(login_url='register') #changes
def min_cart(request, product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cart_id')
            ct_list = cartlist.objects.filter(cart_id=cart_id)

    # ct=cartlist.objects.get(user=user,cart_id=c_id(request)

        if ct_list.exists():
            for ct in ct_list:
                product = get_object_or_404(shop, id=product_id)
                try:
                    c_items = cartitems.objects.get(product=product, cart=ct)
                    if c_items.quantity>1:
                        c_items.quantity-=1
                        c_items.save()
                    else:
                        c_items.delete()
                except cartitems.DoesNotExist:
                    pass

    except cartlist.DoesNotExist:
        pass

    return redirect('cart')


@login_required(login_url='register') #changes
def cart_delete(request, product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cart_id')
            ct_list = cartlist.objects.filter(cart_id=cart_id)

        if ct_list.exists():
            for ct in ct_list:
                product = get_object_or_404(shop, id=product_id)
                try:
                    c_items = cartitems.objects.get(product=product, cart=ct)
                    c_items.delete()
                except cartitems.DoesNotExist:
                    pass

    except cartlist.DoesNotExist:
        pass

    return redirect('cart')

def check_out(request):
    if request.method == "POST":
            User = request.user
            Cart = cartlist.objects.filter(user=request.user).first()
            First_name = request.POST['first_name']
            Last_name = request.POST['last_name']
            Country = request.POST['country']
            Street_address = request.POST['street_address']
            Town_city = request.POST['town']
            Post_code = request.POST['postcode']
            Phone = request.POST['phone']
            Email = request.POST['email']
    
            data_checkout = checkout(
                user=User,
                cart=Cart,
                firstname=First_name,
                lastname=Last_name, 
                country=Country,
                address=Street_address, 
                city=Town_city, 
                postcode=Post_code, 
                phone=Phone, 
                email=Email
            )
            data_checkout.save()
            return redirect('payment')
    return render(request,'checkout.html')

def payments(request):
    if request.method == "POST":
        hi=request.user
        Account_number = request.POST["account_number"]  
        Name = request.POST['name']
        Expiry_month = request.POST['expiry_month']
        Expiry_year = request.POST['expiry_year']
        Cvv = request.POST['cvv']

        data_payment = payment(
            user=hi,
            account_number=Account_number,
            name=Name,
            expiry_month=Expiry_month,
            expiry_year=Expiry_year,
            cvv=Cvv,
        )
        data_payment.save()
        return redirect("pay")
    return render(request, 'payment.html')

def pay(request):
    return render(request, 'pay.html')