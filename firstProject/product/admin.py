from django.contrib import admin
from .models import product,category
# Register your models here.


@admin.register(product)
class product_admin(admin.ModelAdmin):
    list_display = ('id','product_name','product_description','product_price','product_brand','category')    
 
@admin.register(category)
class category_admin(admin.ModelAdmin):
    list_display = ('id','category_name','slug')
    
   
# admin.site.register(Category,category_admin)
#admin.site.register(product)