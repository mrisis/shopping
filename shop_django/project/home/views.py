from django.shortcuts import render
from django.views import View
from . models import Product
class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')


class MenuView(View):
    def get(self,request):
        products = Product.objects.filter(availabel=True)
        return render(request,'home/menu.html',{'products':products})