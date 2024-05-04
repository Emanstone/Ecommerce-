from django.contrib import admin
from  .models import Category, Product

# Register your models here.

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['category_id','name', 'category_image', 'date']  # category_image here is the image method name in the category model


@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ['product_id','name', 'user', 'vendor', 'product_image', 'date'] # same explained above ; this for the product model   






