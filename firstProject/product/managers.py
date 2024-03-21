from django.db import models

class Product_Manager(models.Manager):
    
    def get_queryset(self):
        # return super().get_queryset().order_by('product_name')
        # return super().get_queryset().order_by('product_brand')
        # return super().get_queryset().filter(product_price__gte = 700)
        # return super().get_queryset(self.model).getPawsIndia()
        return ProductQuerySet(self.model)
    
    def sorted(self):
        return super().get_queryset().order_by('product_name')
    
    def sortByPrice(self):
        return super().get_queryset().order_by('product_price')
    
    def query(self,query):
        return super().get_queryset().filter(product_name__icontains=query)
    
    
class ProductQuerySet(models.QuerySet):
    
    def getPawsIndia(self):
        return self.filter(product_brand = 'PawsUp')
    
    def dog_products(self):
        return self.filter(product_name__icontains = 'dog')
    
    def catProducts(self):
        return self.filter(product_name__icontains = 'cat')