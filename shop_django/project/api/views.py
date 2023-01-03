from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer , ProfileEditSerializer , ProductListSerializer ,\
    CategoryListSerializer,ProductDetailSerializer , CommentSerializer , CommentReplySerializer
from accounts.models import User
from rest_framework import generics
from home.models import Product , Category , Comment
from bucket import bucket



# accounts app api views

class ProfileApiView(APIView):

    def get(self,request,user_id):
        user =User.objects.get(id=user_id)
        ser_data = ProfileSerializer(instance=user)
        return Response(ser_data.data , status = status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    def put(self,request,user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileEditSerializer(instance=user , data=request.data,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)


# home app api views

class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.filter(availabel=True)
    serializer_class = ProductListSerializer

class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.filter(is_sub=False)
    serializer_class = CategoryListSerializer


class ProductDetailApiView(APIView):
    def get(self,request,prdoct_slug):
        product = Product.objects.get(slug=prdoct_slug)
        ser_data = ProductDetailSerializer(instance=product)
        return Response(ser_data.data , status = status.HTTP_200_OK)

class BucketListApiView(APIView):
    def get(self,request):
        bucket_data = bucket.get_objects()
        return Response(bucket_data['Contents'] , status = status.HTTP_200_OK)


class BucketDeleteApiView(APIView):
    def delete(self,request):
        bucket.delete_object()
        return Response( data={'message':'deleted bucket object'},status = status.HTTP_200_OK)

class BucketDownloadApiView(APIView):
    def get(self,request):
        bucket.download_object()
        return Response(data={'message':'downloaded bucket object'} , status=status.HTTP_200_OK)


class CommentCreateApiView(APIView):
    def post(self,request):
        user = request.user
        product = Product.objects.get(id=request.data['product'])
        ser_data = CommentSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save(user=user,product=product)
            return Response(ser_data.data , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)



class CommentReplyApiView(APIView):
    def post(self,request , comment_id):
        user = request.user
        comment = Comment.objects.get(id=comment_id)
        ser_data = CommentReplySerializer(data = request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save(user=user,product=comment.product,is_replay=True,replay=comment)
        return Response(ser_data.data , status = status.HTTP_200_OK)






class CommentListApiView(APIView):
    def get(self,request,product_slug):
        product = Product.objects.get(slug=product_slug)
        comments = product.products_comments.all()
        ser_data = CommentSerializer(comments , many = True)
        return Response(ser_data.data , status = status.HTTP_200_OK)



# orders app api views
