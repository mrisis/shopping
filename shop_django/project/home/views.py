from django.shortcuts import render , get_object_or_404 , redirect
from django.views import View
from . models import Product , Category
from . tasks import  all_bucket_objects_task
from . import tasks
from utils import IsAdminUserMixin
from orders.forms import CardAddForm
from . forms import CommetnCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
    form_class_comment= CommetnCreateForm

    def setup(self, request, *args, **kwargs):
        self.product_instance= get_object_or_404(Product,pk=kwargs['product_id'],slug=kwargs['slug'])
        return super().setup(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        form=CardAddForm
        product = get_object_or_404(Product , slug=kwargs['slug'] )
        comments = product.products_comments.filter(is_replay=False)
        return render(request , 'home/detail.html' , {'product':product,'form':form,'comments':comments,'form_comment':self.form_class_comment})
    @method_decorator(login_required)
    def post(self,request,*args,**kwargs):
        form = self.form_class_comment(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.user= request.user
            new_comment.product = self.product_instance
            new_comment.save()
            messages.success(request,'your comment successfully sended.' , 'success')
            return redirect('home:product_detail',self.product_instance.id , self.product_instance.slug)


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
















