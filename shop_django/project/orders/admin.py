from django.contrib import admin
from . models import OrderItem , Order , Coupon
from core.admin import BaseAdmin


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = ['id' , 'user' , 'created' , 'updated' , 'paid','is_deleted']
    list_filter = ('paid',)
    search_fields = ['id']
    inlines = (OrderItemInLine,)


admin.site.register(Coupon)
