from django.contrib import admin
from . models import Category,Product , Comment
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




@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = ['user' , 'product' , 'created' , 'is_deleted']








