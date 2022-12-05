from django.contrib import admin
from . models import OrderItem , Order , Coupon


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'created' , 'updated' , 'paid']
    list_filter = ('paid',)
    inlines = (OrderItemInLine,)


admin.site.register(Coupon)
