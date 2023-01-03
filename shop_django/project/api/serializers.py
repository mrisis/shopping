from rest_framework import serializers
from accounts.models import User
from home.models import Product ,Category

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

# orders app serializers
