from django.urls import path
from . import views


app_name='orders'
urlpatterns=[
    path('cart/' , views.CartView.as_view() , name='cart'),
    path('card/add/<int:product_id>/' , views.CartAddView.as_view() , name='cart_add'),
    apth('cart/remove/<int:product_id>/' , views.CartRemoveView.as_view() , name='cart_remove'),

]