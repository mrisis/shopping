from django.db import models
from django.urls import reverse
from core.models import BaseModel
from accounts.models import User
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    sub_category= models.ForeignKey('self',on_delete=models.CASCADE , related_name='scategory',null=True,blank=True,verbose_name=_('Sub Category'))
    is_sub = models.BooleanField(default=False,verbose_name=_('Is Sub Category'))
    name = models.CharField(max_length=100,verbose_name=_('Name'))
    slug = models.SlugField(max_length=100 , unique=True,verbose_name=_('Slug'))

    class Meta:
        ordering = ('name' , )
        verbose_name = _('Category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def get_absloute_url(self):
        return reverse('home:category_filter',args=[self.slug])



class Product(BaseModel):
    category = models.ManyToManyField(Category , related_name='products',verbose_name=_('Category'))
    name = models.CharField(max_length=100,verbose_name=_('Name'))
    slug = models.SlugField(max_length=100,unique=True,verbose_name=_('Slug'))
    image = models.ImageField(verbose_name=_('Image'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    availabel = models.BooleanField(default=True,verbose_name=_('Availabel'))



    class Meta:
        ordering = ('name',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail',args=[self.id,self.slug])


class Comment(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='comments',verbose_name=_('User'))
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products_comments',verbose_name=_('Product'))
    body = models.TextField(max_length=300,verbose_name=_('Body'))
    replay = models.ForeignKey('Comment',on_delete=models.CASCADE ,related_name='replay_comments',blank=True , null=True,verbose_name=_('Replay'))
    is_replay = models.BooleanField(default=False,verbose_name=_('Is Replay'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'{self.user} - {self.body[:50]}'














