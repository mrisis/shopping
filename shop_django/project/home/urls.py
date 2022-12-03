from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    path('bucket/' , views.BucketHome.as_view() , name='bucket'),
    path('',views.HomeView.as_view(),name='home'),
    path('menu/',views.MenuView.as_view(), name='menu'),
    path('<slug:slug>/', views.ProductDetailView.as_view() , name='product_detail'),
]