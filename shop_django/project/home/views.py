from django.shortcuts import render , get_object_or_404 , redirect
from django.views import View
from . models import Product , Category
from . tasks import  all_bucket_objects_task
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin
from orders.forms import CardAddForm
class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')


class MenuView(View):
    def get(self,request,category_slug=None):
        products = Product.objects.filter(availabel=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category=Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request,'home/menu.html',{'products':products,'categories':categories})


class ProductDetailView(View):
    def get(self,request,slug):
        form=CardAddForm
        product = get_object_or_404(Product , slug=slug )
        return render(request , 'home/detail.html' , {'product':product,'form':form})


class BucketHome(IsAdminUserMixin,View):
    template_name='home/bucket.html'
    def get(self,request):
        objects=all_bucket_objects_task()
        return render(request,self.template_name,{'objects':objects})


class DeleteBucketObject(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.delete_object_task.delay(key)
        messages.success(request,'bucket object successully deleted' , 'success')
        return redirect('home:bucket')

class DownloadBucketObject(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.download_object_task.delay(key)
        messages.success(request,'bucket object successfully downloaded' , 'success')
        return redirect('home:bucket')
















