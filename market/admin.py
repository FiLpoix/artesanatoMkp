from django.contrib import admin
from .models import User, Category, Product, Artisan, Customer

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Artisan)
admin.site.register(Customer)