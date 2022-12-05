from django.db import models
from django.contrib.auth import get_user_model
from home.models import Product
from django.core.validators import MinValueValidator , MaxValueValidator


class Order(models.Model):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(blank=True , null=True , default=None)


    class Meta:
        ordering = ('paid' , '-updated')

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='item_product')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



class Coupon(models.Model):
    code = models.CharField(max_length=30 , unique=True)
    valid_form = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0) , MaxValueValidator(90)])
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.code














