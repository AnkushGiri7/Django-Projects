from django.test import TestCase
from .models import product
# Create your tests here.

class ProductTest(TestCase):
    def setUp(self):
        self.products=product.pm.create(
            product_name="Jadu Ka Challa",
            product_description="Product created for testing",
            product_price=9999,
            product_brand="BabaKaKamal",
        )
        
    def test_check_product(self):
        products=product.pm.get(product_name="Jadu Ka Challa")
        
        self.assertEqual(products.id,self.products.id)
        self.assertEqual(products.product_name,self.products.product_name)
        
    def test_update_product(self):
        products=product.pm.get(product_name="Jadu Ka Challa")
        old_name=products.product_name
        self.product_name="Baba Ki Booti"
        products.save()
        products=product.pm.get(product_name="Jadu Ka Challa")
        self.assertNotEqual(old_name,self.product_name)
        print(self.product_name)
        
    
    def test_fetch_product(self):
        products=product.pm.all()
        count=len(products)
        self.assertGreater(count,0)