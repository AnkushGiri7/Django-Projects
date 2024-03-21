from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add-to-cart/<int:product_id>',views.AddToCart,name='add_to_cart'),
    path('cart/',views.ViewCart,name='viewcart'),
    path('cart/update/<int:cart_item_id>/',views.UpdateCart,name='updatecartitem'),
    path('cart/delete/<int:cart_item_id>/',views.DeleteCart,name='deletecartitem'),
    path('checkout/',views.CheckOut,name='checkout'),
    path('payment/<str:orderId>',views.MakePayment,name='payment'),
    path('successpage/<str:orderId>',views.successPage,name='successpage'),
    # path('emptycart/',views.emptyPage,name='emptycart'),
]
