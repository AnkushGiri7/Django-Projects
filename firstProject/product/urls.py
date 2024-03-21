from django.contrib import admin
from django.urls import path
from .views import product_view,product_detail_view,field_lookup,CategoryDetailView
urlpatterns = [
    path('products/',product_view.as_view()),
    path('products/<int:pk>',product_detail_view.as_view(),name = 'productDetail'),
    path('product_lookup/',field_lookup,name="product_lookup"),
    path('category/<slug:slug>',CategoryDetailView.as_view(),name='category')
]
