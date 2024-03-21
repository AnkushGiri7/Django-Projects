"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from firstApp import views
from product import views as p
from django.conf.urls.static import static 
from firstProject import settings 
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.firstPage,name = 'homepage'),
    # path('home',views.home),
    # path('about',views.about),
    # path('contact',views.contactPage),
    # path('users',views.users),
    # path('login',views.loginuser),
    # path('register',views.register_user),
    # path('submit',views.submit),
    # path('class',views.first_view.as_view()),
    # path('second',views.second_view.as_view(name = "Ajay")),
    path("search/",views.search),
    path("",views.home),
    path("about/",views.about),
    path('product/',include('product.urls')),
    path('register/',views.Register),
    path('login/',views.Login),
    path('logout/',views.Logout,name='logout'),
    path('',include('cart.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
