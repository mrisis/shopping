from django.urls import path
from . import views


app_name='orders'
urlpatterns=[
    path('cart/' , views.CartView.as_view() , name='cart'),
    path('card/add/<int:product_id>/' , views.CartAddView.as_view() , name='cart_add'),
    path('cart/remove/<int:product_id>/' , views.CartRemoveView.as_view() , name='cart_remove'),
    path('cart/create/' , views.OrderCreateView.as_view() , name='order_create'),
    path('detail/<int:order_id>/' , views.OrderDetailView.as_view() , name='orders_detail'),
    path('pay/<int:prder_id>/' , views.OrderPayView.as_view() , name='order_pay'),

]