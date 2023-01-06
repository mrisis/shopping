from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer , ProfileEditSerializer , ProductListSerializer ,\
    CategoryListSerializer,ProductDetailSerializer , CommentSerializer , CommentReplySerializer ,\
    QuantitySerializer , OrderSerializer
from rest_framework import generics
from home.models import Product , Category , Comment
from bucket import bucket
from orders.cart import Cart
from accounts.models import User
from orders.models import Order , OrderItem



# accounts app api views

class ProfileApiView(APIView):

    def get(self,request,user_id):
        user =User.objects.get(id=user_id)
        ser_data = ProfileSerializer(instance=user)
        return Response(ser_data.data , status = status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    '''
        method put:
          for edit and update user profile


    '''
    def put(self,request,user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileEditSerializer(instance=user , data=request.data,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)


# home app api views

class ProductListApiView(generics.ListAPIView):
    '''
        method get:
            for get all products
    '''
    queryset = Product.objects.filter(availabel=True)
    serializer_class = ProductListSerializer

class CategoryListApiView(generics.ListAPIView):

    '''
        method get:
            for get all categories
    '''



    queryset = Category.objects.filter(is_sub=False)
    serializer_class = CategoryListSerializer


class ProductDetailApiView(APIView):

    '''
        method get:
            for get product detail
    '''
    def get(self,request,prdoct_slug):
        product = Product.objects.get(slug=prdoct_slug)
        ser_data = ProductDetailSerializer(instance=product)
        return Response(ser_data.data , status = status.HTTP_200_OK)

class BucketListApiView(APIView):

    '''
        method get:
            for get all bucket objects in arvan cloud
    '''
    def get(self,request):
        bucket_data = bucket.get_objects()
        return Response(bucket_data['Contents'] , status = status.HTTP_200_OK)


class BucketDeleteApiView(APIView):

    '''
        method delete:
            for delete bucket object in arvan cloud
    '''
    def delete(self,request):
        bucket.delete_object()
        return Response( data={'message':'deleted bucket object'},status = status.HTTP_200_OK)

class BucketDownloadApiView(APIView):

    '''
        method get:
            for download bucket object in arvan cloud
    '''
    def get(self,request):
        bucket.download_object()
        return Response(data={'message':'downloaded bucket object'} , status=status.HTTP_200_OK)


class CommentCreateApiView(APIView):

    '''
        method post:
            for create comment
    '''
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
    def get(self,request,product_slug):
        product = Product.objects.get(slug=product_slug)
        comments = product.products_comments.all()
        ser_data = CommentSerializer(comments , many = True)
        return Response(ser_data.data , status = status.HTTP_200_OK)

# orders app api views

class CartApiView(APIView):

    '''
        method get:
            for get all cart items
    '''


    def get(self,request):
        cart = Cart(request)
        return Response(cart.cart , status = status.HTTP_200_OK)


class CartAddAPiView(APIView):

    '''
        method post:
            for add product item to cart
    '''

    def post(self,request,product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        ser_data = QuantitySerializer(data=request.data)
        if ser_data.is_valid():
            cart.add(product=product,quantity=ser_data.data['quantity'])
            return Response(cart.cart , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)


class CartRemoveApiView(APIView):

    '''
        method delete:
            for remove product item form cart
    '''
    def delete(self,request,product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.remove(product)
        return Response(cart.cart , status = status.HTTP_200_OK)



class OrderCreateApiView(APIView):

    '''
        method post:
            for create order and save order in database
    '''
    def post(self,request):
        order = Order.objects.create(user=request.user)
        cart = Cart(request)
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
        cart.clear()
        ser_data = OrderSerializer(instance=order)
        result = ser_data.data
        result['message'] = 'order created'
        return Response(result , status = status.HTTP_200_OK)



class OrderDetailApiView(APIView):

    '''
        method get:
            for get order detail and show order items
    '''
    def get(self,request,order_id):
        order = Order.objects.get(id=order_id)
        ser_data = OrderSerializer(instance=order)
        return Response(ser_data.data , status = status.HTTP_200_OK)














































