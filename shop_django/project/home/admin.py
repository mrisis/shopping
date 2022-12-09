from django.contrib import admin

from accounts import models
from . models import Category,Product
from core.admin import BaseAdmin
from django.contrib import admin



@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ('name','price','availabel','is_active','is_deleted')
    row_id_fields=('category',)
    prepopulated_fields = {'slug':('name',)}




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','is_sub','sub_category')
    prepopulated_fields = {'slug':('name',)}
