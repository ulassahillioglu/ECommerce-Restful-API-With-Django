from rest_framework import generics
from .models import FavProduct, Order, Product,Categories,Onsale
from .serializers import FavProductSerializer, OrderSerializer, ProductsSerializer,CategoriesSerializer,OnsaleSerializer
from rest_framework import status
from rest_framework.response import Response

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductsSerializer
    
    def get_queryset(self):
        # return super().get_queryset()
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('categoryId')
        if category_id is not None:
            queryset = queryset.filter(categoryId=category_id)
        return queryset

class FavProductList(generics.ListCreateAPIView):
    serializer_class = FavProductSerializer
    
    def get_queryset(self):
        queryset = FavProduct.objects.all()
        user_id = self.request.query_params.get('userId')
        id = self.request.query_params.get('id')
        if user_id is not None:
            queryset = queryset.filter(userId=user_id)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
    def post_queryset(self, fav_product):
        # Create a new FavProduct instance
        fav_product_instance = FavProduct.objects.create(**fav_product)
        # You may need to save the instance if necessary
        # fav_product_instance.save()
        return fav_product_instance

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.query_params.get('userId')
        
        # Call post_queryset method to create FavProduct
        fav_product_instance = self.post_queryset(serializer.validated_data)
        
        # Serialize the created FavProduct instance
        serializer = self.get_serializer(fav_product_instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def delete_queryset(self, fav_product_id):
        # Filter FavProduct instance based on the provided id
        fav_product_instance = FavProduct.objects.filter(id=fav_product_id).first()
        return fav_product_instance

    
    def delete(self, request, *args, **kwargs):
        # Extract id from query parameters
        fav_product_id = request.query_params.get('id')

        # Call delete_queryset with the extracted id
        fav_product_instance = self.delete_queryset(fav_product_id)

        # Check if the instance exists before deleting
        if fav_product_instance:
            fav_product_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'FavProduct not found'}, status=status.HTTP_404_NOT_FOUND)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    
class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        # return super().get_queryset()
        queryset = Order.objects.all()
        userId = self.request.query_params.get('userId')
        if userId is not None:
            queryset = queryset.filter(userId=userId)
        return queryset 
    
class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    
class OnSaleList(generics.ListCreateAPIView):
    serializer_class = OnsaleSerializer
    queryset = Onsale.objects.all()