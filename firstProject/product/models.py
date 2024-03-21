from django.db import models
from .managers import Product_Manager
from autoslug import AutoSlugField
# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100,name='category_name')
    slug=AutoSlugField(populate_from='category_name')
    
    def __str__(self):
        return self.category_name
    
class product(models.Model):
    product_name = models.CharField(max_length = 100,default ="product_Name")
    product_description = models.TextField(default='Description')
    product_price = models.IntegerField(default=0)
    product_brand = models.CharField(max_length=75,default='Brand_Name')
    product_image = models.ImageField(upload_to='images/',default='')
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    # category=models.ForeignKey(category,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(category,on_delete=models.PROTECT,null=True)
    
    pm = models.Manager()
    cm = Product_Manager()
    
    def __str__(self):
        return self.product_name
    