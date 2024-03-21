from django.contrib.auth.signals import *
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *
from .models import product


@receiver(user_logged_in,sender=User)
def log_in(sender,request,user,**kwargs):
    print("****************************")
    print("Logged In Successfully")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguments:",kwargs)
    print("****************************")
    
@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("****************************")
    print("Logged out Successfully")    
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguments:",kwargs)
    print("****************************")
    

@receiver(post_save,sender=product)
def product_create_signal(sender,instance,**kwargs):
    print("*******************************************************************")
    print("************************Product Created****************************")
    print("*******************************************************************")
    print("sender:",sender)
    print("instance:",instance)
    print("Arguments:",kwargs)
    print("*******************************************************************")
    
@receiver(post_delete,sender=product)
def product_delete_signal(sender,instance,**kwargs):
    print("*******************************************************************")
    print("************************Product Deleted****************************")
    print("*******************************************************************")
    print("sender:",sender)
    print("instance:",instance)
    print("Arguments:",kwargs)
    print("*******************************************************************")