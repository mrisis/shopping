from django.shortcuts import render
from django.views import View


class CartView(View):
    def get(self,request):
        return render(request,'orders/cart.html')
