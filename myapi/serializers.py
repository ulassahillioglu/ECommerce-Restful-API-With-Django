from rest_framework import serializers
from .models import Categories, FavProduct, Onsale, Order, Product

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

    def fetch_id(self):
        return self.fields
    
class OnsaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onsale
        fields = ['id', 'name', 'price', 'description', 'category', 'imageUrl', 'instock', 'ordercount','productId']

class ProductsSerializer(serializers.ModelSerializer):
    # categoryid = CategoriesSerializer().fetch_id()
    # Serialize the related category
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'categoryId', 'imageUrl', 'inStock', 'orderCount']
    def fetch_id(self):
        return self.fields

class FavProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavProduct
        fields = ['id','name','price','description','imageUrl','date_added','userId']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','name','price','description','imageUrl','date_added','userId']