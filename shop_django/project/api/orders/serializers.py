from rest_framework import serializers
from orders.models import Order , OrderItem


class QuantitySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('order_items','user' , 'paid' , 'discount')

    def get_order_items(self,obj):
        order_items = obj.items.all()
        return OrderItemSerializer(order_items,many=True).data

