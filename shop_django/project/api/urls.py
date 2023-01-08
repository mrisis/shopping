from django.urls import path
from . import views
from api.accounts import views as accounts_views
from api.home import views as home_views
from api.orders import views as orders_views

app_name = 'api'

urlpatterns = [
    # accounts apis urls

    path('profile/<int:user_id>/' , accounts_views.ProfileApiView.as_view() , name='profile_api'),
    path('profile/edit/<int:user_id>/',accounts_views.ProfileEditApiView.as_view() , name='profile_edit_api'),


    # home apis urls

    path('product/list/' , home_views.ProductListApiView.as_view() , name='product_list_api'),
    path('category/list/' , home_views.CategoryListApiView.as_view() , name='category_list_api'),
    path('product/detail/<str:prdoct_slug>/' , home_views.ProductDetailApiView.as_view() , name='product_detail_api'),
    path('bucket/' , home_views.BucketListApiView.as_view() , name='bucket_api'),
    path('bucket/delete/' , home_views.BucketDeleteApiView.as_view() , name='bucket_delete_api'),
    path('bucket/download/' , home_views.BucketDownloadApiView.as_view() , name='bucket_download_api'),

    path('comment/create/',home_views.CommentCreateApiView.as_view() , name='comment_create_api'),
    path('reply/create/<int:comment_id>/',home_views.CommentReplyApiView.as_view() , name='reply_create_api'),
    path('comment/list/<slug:product_slug>/',home_views.CommentListApiView.as_view() , name='comment_list_api'),


    #orders apis urls

    path('cart/',orders_views.CartApiView.as_view() , name='cart_api'),
    path('cart/add/<int:product_id>/',orders_views.CartAddAPiView.as_view() , name='cart_add_api'),
    path('cart/remove/<int:product_id>/',orders_views.CartRemoveApiView.as_view() , name='cart_remove_api'),
    path('order/create/',orders_views.OrderCreateApiView.as_view() , name='order_create_api'),
    path('order/detail/<int:order_id>/' , orders_views.OrderDetailApiView.as_view() , name = 'order_detail_api'),


]