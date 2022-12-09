from django.db import models
from django.urls import reverse
from core.models import BaseModel
from accounts.models import User

class Category(models.Model):
    sub_category= models.ForeignKey('self',on_delete=models.CASCADE , related_name='scategory',null=True,blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique=True)

    class Meta:
        ordering = ('name' , )
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absloute_url(self):
        return reverse('home:category_filter',args=[self.slug])



class Product(BaseModel):
    category = models.ManyToManyField(Category , related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    availabel = models.BooleanField(default=True)



    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail',args=[self.slug])


class Comment(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='comments')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products_comments')
    body = models.TextField(max_length=300)
    replay = models.ForeignKey('Comment',on_delete=models.CASCADE ,related_name='replay_comments',null=True,blank=True)
    is_replay = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.body[:50]}'














