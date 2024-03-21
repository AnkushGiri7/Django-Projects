from django.shortcuts import render,get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
from product.models import product
from .models import Cart,CartItem
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def AddToCart(request,product_id):
    products=get_object_or_404(product,id=product_id)
    print(products.product_name)
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    print(created)
    item,item_created=CartItem.objects.get_or_create(cart=cart,product=products)
    quantity=request.GET.get("quantity")
    if not item_created:
        item.quantity+=int(quantity)
    else:
        item.quantity=1
    item.save()
    return HttpResponseRedirect("/product/product_lookup/")
    

def ViewCart(request):
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItem=cart.cartitem_set.all()
    # print(cartItem)
    final_amount=0
    for item in cartItem:
        final_amount+=item.quantity*item.product.product_price
    return render(request,"viewcart.html",{"items":cartItem,"finalAmount":final_amount,"created":created})



def UpdateCart(request,cart_item_id):
    current_cart_item=get_object_or_404(CartItem,pk=cart_item_id)
    quantity=request.GET.get("quantity")
    current_cart_item.quantity=int(quantity)
    current_cart_item.save()
    return HttpResponseRedirect("/cart/")

def DeleteCart(request,cart_item_id):
    current_cart_item=get_object_or_404(CartItem,pk=cart_item_id)
    current_cart_item.delete()
    # current_cart_item.save()
    return HttpResponseRedirect("/cart/")

from .forms import OrderForm
from .models import Order,OrderItem
import uuid
def CheckOut(request):
    currentUser=request.user
    initial={
        "user":currentUser,
        # "first_name":currentUser.get_firstname(),
        # "email":currentUser.email()
    }
    print(initial["user"])
    form = OrderForm(initial=initial)
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItem=cart.cartitem_set.all()
    final_amount=0
    for item in cartItem:
        final_amount+=item.quantity*item.product.product_price
    
    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            user=request.user
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phone_no=form.cleaned_data['phone_no']
            orderId=str(uuid.uuid4())
            
            order=Order.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                city=city,
                state=state,
                pincode=pincode,
                phone_no=phone_no,
                order_id=orderId[:20]
            )
            for item in cartItem:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    total=item.quantity*item.product.product_price
                )
        
        return HttpResponseRedirect("/payment/"+orderId[:20])
    
    context = {"form":form,"cartItem":cartItem,"final_amount":final_amount}
    return render(request,"checkout.html",context)


import razorpay
import setuptools
def MakePayment(request,orderId):
    order=Order.objects.get(pk=orderId)
    order_item=order.orderitem_set.all()
    amount=0
    for item in order_item:
        amount+=item.total
    print(amount)
    client = razorpay.Client(auth=("rzp_test_zsG4MlhPV9isuO", "zIjfwFndgEldw1LIqaTB4LkN"))

    data = { "amount": amount*100, "currency": "INR", "receipt": orderId,"payment_capture":1}
    payment = client.order.create(data=data)
    return render(request,"payment.html",{"payment":payment})

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
@csrf_exempt
def successPage(request,orderId):
    if request.method =='POST':
        client = razorpay.Client(auth=("rzp_test_zsG4MlhPV9isuO", "zIjfwFndgEldw1LIqaTB4LkN"))
        check=client.utility.verify_payment_signature({
        'razorpay_order_id': request.POST.get('razorpay_order_id'),
        'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
        'razorpay_signature': request.POST.get('razorpay_signature')
        })
        print(check)
        
        
        if check:
            order=Order.objects.get(pk=orderId)
            order.paid=True
            order.save()
            # if order.paid:
            currentUser=request.user
            cart=Cart.objects.get(user=currentUser)
            cart.delete()
            # return render(request,"emptycart.html",{})
            orderitems=order.orderitem_set.all()
            send_mail(
                "Order Placed....",#subject part
                "Order is Placed and it will be dilivered in 3-4 days",#message part
                settings.EMAIL_HOST_USER,
                ["ankushgiri519@gmail.com","priyanka.vibhute@itvendant.com"],
                fail_silently=False,
                html_message=render_to_string("email.html",{"item":orderitems})
            )
            return render(request,"successpage.html",{})
        else:
            return render(request,"failpage.html",{})
        
        


# @login_required
# def emptyPage(request):
    
#     user=request.user
#     cart=Cart.objects.get(user=user)
    
#         return render(request,"emptycart.html",{})
        