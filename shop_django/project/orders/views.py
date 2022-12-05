from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . cart import Cart
from home.models import Product
from . forms import CardAddForm
from . models import Order , OrderItem
class CartView(View):
    def get(self,request):
        cart=Cart(request)
        return render(request,'orders/cart.html',{'cart':cart})


class CartAddView(View):
    def post(self,request,product_id):
        cart = Cart(request)
        product = get_object_or_404(Product,id=product_id)
        form = CardAddForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            cart.add(product,cd['quantity'])
        return redirect('orders:cart')

class CartRemoveView(View):
    def get(self,request,product_id):
        cart = Cart(request)
        product = get_object_or_404(Product , id=product_id)
        cart.remove(product)
        return redirect('orders:cart')


class OrderDetailView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        order = get_object_or_404(Order , id=order_id)
        return render(request,'orders/order.html' , {'order':order})

class OrderCreateView(LoginRequiredMixin,View):
    def get(self,request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)

        for item in cart :
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'] , quantity=item['quantity'])
            cart.clear()

        return redirect('orders:orders_detail',order.id)



















