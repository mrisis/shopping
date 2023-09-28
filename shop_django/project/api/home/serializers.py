from rest_framework import serializers
from home.models import Product , Category , Comment





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
