from django.shortcuts import render , get_object_or_404 , redirect
from django.views import View
from . models import Product , Category , Comment
from . tasks import  all_bucket_objects_task
from . import tasks
from utils import IsAdminUserMixin
from orders.forms import CardAddForm
from . forms import CommetnCreateForm , CommentReplayForm , ProductSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.translation import activate,get_language
from django.contrib.sessions.models import Session
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/home.html'



class MenuView(View):
    def get(self,request,slug_cateory=None):
        form_search = ProductSearchForm
        products = Product.objects.filter(availabel=True)
        p=Paginator(Product.objects.filter(availabel=True),3)
        page = request.GET.get('page')
        productspage = p.get_page(page)
        if request.GET.get('search'):
            products = products.filter(name__contains=request.GET['search'])
            p = Paginator(products, 2)
            page = request.GET.get('page')
            productspage = p.get_page(page)


        categories = Category.objects.filter(is_sub=False)
        if slug_cateory:
            category=Category.objects.get(slug=slug_cateory)
            products = products.filter(category=category)
            p = Paginator(products, 2)
            page = request.GET.get('page')
            productspage = p.get_page(page)

        return render(request,'home/menu.html',{'products':products,'categories':categories ,'form_search':form_search , 'productspage':productspage})


class ProductDetailView(View):
    form_class_comment= CommetnCreateForm
    form_replay=CommentReplayForm

    def setup(self, request, *args, **kwargs):
        self.product_instance= get_object_or_404(Product,pk=kwargs['product_id'],slug=kwargs['slug'])
        return super().setup(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        form=CardAddForm
        product = get_object_or_404(Product , slug=kwargs['slug'] )
        comments = product.products_comments.filter(is_replay=False)
        return render(request , 'home/detail.html' , {'product':product,'form':form,'comments':comments,'form_comment':self.form_class_comment,'replay_form':self.form_replay})
    @method_decorator(login_required)
    def post(self,request,*args,**kwargs):
        form = self.form_class_comment(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.user= request.user
            new_comment.product = self.product_instance
            new_comment.save()
            messages.success(request,_('your comment successfully sended.') , 'success')
            return redirect('home:product_detail',self.product_instance.id , self.product_instance.slug)


class BucketHome(IsAdminUserMixin,View):
    template_name='home/bucket.html'
    def get(self,request):
        objects=all_bucket_objects_task()
        return render(request,self.template_name,{'objects':objects})


class DeleteBucketObject(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.delete_object_task.delay(key)
        messages.success(request,_('bucket object successully deleted') , 'success')
        return redirect('home:bucket')

class DownloadBucketObject(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.download_object_task.delay(key)
        messages.success(request,_('bucket object successfully downloaded') , 'success')
        return redirect('home:bucket')


class ProductAddReplayView(LoginRequiredMixin,View):
    form_class = CommentReplayForm
    def post(self,request,product_id,comment_id):
        product = get_object_or_404(Product,id=product_id)
        comment = get_object_or_404(Comment , id=comment_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.user = request.user
            replay.product = product
            replay.replay=comment
            replay.is_replay = True
            replay.save()
            messages.success(request,_('your replay successfully sended.'))

        return redirect('home:product_detail',product.id,product.slug)



class ChangeLanguageView(View):
    def get(self,request):
        activate(request.GET.get('lang'))

        print(get_language())
        return redirect(request.GET.get('next'))










