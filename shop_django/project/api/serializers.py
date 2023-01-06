from rest_framework import serializers
from accounts.models import User
from home.models import Product ,Category , Comment
from orders.models import Order , OrderItem

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','full_name','email','phone_number','image','is_active','is_admin','is_superuser')


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name','email','phone_number')


# home app serializers

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','slug','category','image','description','price','availabel')

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','slug','is_sub','sub_category')

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name' , 'image' , 'description' , 'price')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ( 'user','product' , 'body' , 'is_replay' , 'replay','replies')

    def get_user(self,obj):
        return obj.user.email

    def get_replies(self,obj):
        replies = obj.replay_comments.all()
        return CommentReplySerializer(replies,many=True).data

class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('user','body')

    def get_user(self,obj):
        return obj.user.email



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



class CouponApplSerializer(serializers.Serializer):
    code = serializers.CharField()




















