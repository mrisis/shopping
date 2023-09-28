from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.cart import Cart
from home.models import Product
from .serializers import QuantitySerializer , OrderSerializer
from orders.models import Order , OrderItem





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
    # def post(self,request):
    #     order = Order.objects.create(user=request.user)
    #     cart = Cart(request)
    #     for item in cart:
    #         OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
    #     cart.clear()
    #     ser_data = OrderSerializer(instance=order)
    #     result = ser_data.data
    #     result['message'] = 'order created'
    #     return Response(result , status = status.HTTP_200_OK)

    def post(self, request):
        order = Order.objects.create(user=request.user)
        cart = Cart(request)
        order_items = [OrderItem(order=order, product=item['product'], price=item['price'], quantity=item['quantity']) for item in cart]

        OrderItem.objects.bulk_create(order_items)
        cart.clear()
        ser_data = OrderSerializer(instance=order)
        result = ser_data.data
        result['message'] = 'order created'
        return Response(result, status=status.HTTP_200_OK)


class OrderDetailApiView(APIView):

    '''
        method get:
            for get order detail and show order items
    '''
    def get(self,request,order_id):
        order = Order.objects.get(id=order_id)
        ser_data = OrderSerializer(instance=order)
        return Response(ser_data.data , status = status.HTTP_200_OK)



