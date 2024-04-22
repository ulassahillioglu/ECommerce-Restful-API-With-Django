from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.TextField(blank=True, null=False,default="")

    class Meta:
        db_table = 'categories'

class FavProduct(models.Model):
    name = models.TextField(blank=True, null=False,default="")
    price = models.FloatField(blank=True, null=False,default=0.0)
    description = models.TextField(blank=True, null=False,default="")
    imageUrl = models.TextField(db_column='imageUrl', null=False,default="")
    date_added = models.DateField(auto_now_add=False)
    userId = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "favProducts"
        
    @classmethod
    def create_fav_product(cls, user_id, **kwargs):
        # Create and return a new FavProduct instance
        return cls.objects.create(userId_id=user_id, **kwargs)

class Order(models.Model):
    name = models.TextField(blank=True, null=False,default="")
    price = models.FloatField(blank=True, null=False,default=0.0)
    description = models.TextField(blank=True, null=False,default="")
    imageUrl = models.TextField(db_column='imageUrl', null=False,default="")
    date_added = models.DateField(auto_now_add=False)
    userId = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "orders"

class Product(models.Model):
    name = models.TextField(blank=True, null=False,default="")
    price = models.FloatField(blank=True, null=False,default=0.0)
    description = models.TextField(blank=True, null=False,default="")
    category = models.TextField(blank=True, null=False,default="")
    categoryId = models.ForeignKey(Categories, db_column='categoryId', blank=True, null=True, on_delete=models.CASCADE,default="")  # Field name made lowercase.
    imageUrl = models.TextField(db_column='imageUrl', null=False,default="")  # Field name made lowercase.
    inStock = models.IntegerField(db_column='inStock', blank=True, null=False,default=0)  # Field name made lowercase.
    orderCount = models.IntegerField(db_column='orderCount', blank=True, null=False,default=0)  # Field name made lowercase.

    class Meta:
        db_table = 'products'
        
class Onsale(models.Model):
    name = models.CharField(max_length=250,blank=True, null=False,default="")
    price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=False,default=0.0)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float    
    description = models.TextField(blank=True, null=False,default="")
    category = models.CharField(max_length=20,blank=True, null=False,default="")
    imageUrl = models.CharField(db_column='image_url',max_length=250,blank=True, null=False,default="")
    instock = models.IntegerField(db_column='inStock', blank=True, null=False,default=0)  # Field name made lowercase.
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=False,default=0)  # Field name made lowercase.
    productId = models.ForeignKey(Product, db_column='productId', on_delete=models.CASCADE, default=None, blank=True, null=True)


    class Meta:
        db_table = 'onSale'