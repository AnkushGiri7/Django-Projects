from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import product,category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class product_view(ListView):
    model = product
    template_name = "products.html"
    
class product_detail_view(DetailView):
    model = product
    template_name = "product_detail.html"
    context_object_name = 'p'
    
def field_lookup(request):
    # products=product.cm.all()
    # products=product.pm.all()
    # products=product.pm.all().filter(Q(id=8)&Q(product_name="Dogs Bites")) 
    # products=product.pm.all().filter(Q(product_price__lte='3000')&Q(product_name__icontains="dog")) 
    # products=product.pm.all().filter(Q(id=9) | Q(id=10)) 
    products=product.pm.all().filter(~Q(product_brand='PawsUp'))# ~ -> means not 
    return render(request,"product_lookup.html",{"product" : products})
    

class CategoryDetailView(DetailView):
    model=category
    template_name="category.html"
    context_object_name="category"
    slug_field="slug"
    
    
