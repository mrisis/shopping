from django.contrib import admin
from . models import Category,Product , Comment
from core.admin import BaseAdmin
from django.contrib import admin



@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ('name','price','availabel','is_active','is_deleted')
    raw_id_fields=('category',)
    search_fields = ('name','price')
    prepopulated_fields = {'slug':('name',)}




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','is_sub','sub_category')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}




@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = ['user' , 'product' , 'created' , 'is_deleted']
    raw_id_fields = ['user' , 'product' , 'replay']
    search_fields = ['user', 'text']








