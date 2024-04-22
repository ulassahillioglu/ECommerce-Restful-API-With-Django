from django.contrib import admin
from .models import Product, Categories, Onsale

admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Onsale)

