from django.urls import path
from .views import OrderList, ProductList, CategoryList, CategoryDetail, ProductDetail, OnSaleList,FavProductList


urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('', ProductList.as_view(), name='product_list'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('on-sale',OnSaleList.as_view(),name='on_sale'),
    path('fav-products/', FavProductList.as_view(),name="fav_products"),
    path('orders/', OrderList.as_view(),name="orders")
    
    # path('^products?categoryId=P<categoryId>/',views.product_category,name='product_by_category')
  
]