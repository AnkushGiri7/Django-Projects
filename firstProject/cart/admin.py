from django.contrib import admin
from .models import Cart,CartItem,Order,OrderItem
# Register your models here.
# @admin.register(Cart)
# class cart_admin(admin.ModelAdmin):
#     list_display=()
    

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]      #foreign key is needed to do this
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
    
# @admin.register(CartItem)
# class cart_item_admin(admin.ModelAdmin):
#     list_display=('quantity')