from django.db import models
from django.contrib.auth import get_user_model
from home.models import Product
from django.core.validators import MinValueValidator , MaxValueValidator
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Order(BaseModel):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='orders', verbose_name=_('user'))
    paid = models.BooleanField(default=False, verbose_name=_('paid'))
    discount = models.IntegerField(blank=True , null=True , default=None,verbose_name=_('discount'))


    class Meta:
        ordering = ('paid' , '-updated')
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items', verbose_name=_('order'))
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='item_product', verbose_name=_('product'))
    price = models.IntegerField(verbose_name=_('price'))
    quantity = models.IntegerField(default=1,verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItems')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



class Coupon(models.Model):
    code = models.CharField(max_length=30 , unique=True, verbose_name=_('code'))
    valid_form = models.DateTimeField(verbose_name=_('valid_form'))
    valid_to = models.DateTimeField(verbose_name=_('valid_to'))
    discount = models.IntegerField(validators=[MinValueValidator(0) , MaxValueValidator(90)], verbose_name=_('discount'))
    active = models.BooleanField(default=False,verbose_name=_('active'))

    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')


    def __str__(self):
        return self.code














