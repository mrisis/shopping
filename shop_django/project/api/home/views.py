
from rest_framework import pagination
from rest_framework import permissions
from home.models import Product ,Category , Comment
from .serializers import ProductListSerializer , CategoryListSerializer , ProductDetailSerializer , CommentSerializer , CommentReplySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bucket import bucket




class ProductListApiView(generics.ListAPIView):
    '''
        method get:
            for get all products
    '''

    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination
    queryset = Product.objects.filter(availabel=True)
    serializer_class = ProductListSerializer


class CategoryListApiView(generics.ListAPIView):

    '''
        method get:
            for get all categories
    '''

    permission_classes = [permissions.IsAuthenticated]

    queryset = Category.objects.filter(is_sub=False)
    serializer_class = CategoryListSerializer



class ProductDetailApiView(APIView):

    '''
        method get:
            for get product detail
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,prdoct_slug):
        product = Product.objects.get(slug=prdoct_slug)
        self.check_object_permissions(request,product)
        ser_data = ProductDetailSerializer(instance=product)
        return Response(ser_data.data , status = status.HTTP_200_OK)


class BucketListApiView(APIView):

    '''
        method get:
            for get all bucket objects in arvan cloud
    '''

    permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]
    def get(self,request):
        bucket_data = bucket.get_objects()
        return Response(bucket_data['Contents'] , status = status.HTTP_200_OK)


class BucketDeleteApiView(APIView):

    '''
        method delete:
            for delete bucket object in arvan cloud
    '''

    permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]
    def delete(self,request):
        bucket.delete_object()
        return Response( data={'message':'deleted bucket object'},status = status.HTTP_200_OK)

class BucketDownloadApiView(APIView):

    '''
        method get:
            for download bucket object in arvan cloud
    '''

    permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]
    def get(self,request):
        bucket.download_object()
        return Response(data={'message':'downloaded bucket object'} , status=status.HTTP_200_OK)




class CommentCreateApiView(APIView):

    '''
        method post:
            for create comment
    '''

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        product = Product.objects.get(id=request.data['product'])
        ser_data = CommentSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save(user=user,product=product)
            return Response(ser_data.data , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)



class CommentReplyApiView(APIView):

    '''
        method post:
            for create comment reply
    '''

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request , comment_id):
        user = request.user
        comment = Comment.objects.get(id=comment_id)
        ser_data = CommentReplySerializer(data = request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save(user=user,product=comment.product,is_replay=True,replay=comment)
        return Response(ser_data.data , status = status.HTTP_200_OK)


class CommentListApiView(APIView):

    '''
        method get:
            for get all comments of product and reply comments
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,product_slug):
        product = Product.objects.get(slug=product_slug)
        comments = product.products_comments.all()
        ser_data = CommentSerializer(comments , many = True)
        return Response(ser_data.data , status = status.HTTP_200_OK)
