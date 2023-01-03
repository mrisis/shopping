from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('profile/<int:user_id>/' , views.ProfileApiView.as_view() , name='profile_api'),
    path('profile/edit/<int:user_id>/',views.ProfileEditApiView.as_view() , name='profile_edit_api'),
    path('product/list/' , views.ProductListApiView.as_view() , name='product_list_api'),
    path('category/list/' , views.CategoryListApiView.as_view() , name='category_list_api'),
    path('product/detail/<str:prdoct_slug>/' , views.ProductDetailApiView.as_view() , name='product_detail_api'),

]