from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('profile/<int:user_id>/' , views.ProfileApiView.as_view() , name='profile_api'),
    path('profile/edit/<int:user_id>/',views.ProfileEditApiView.as_view() , name='profile_edit_api'),
    path('product/list/' , views.ProductListApiView.as_view() , name='product_list_api'),
    path('category/list/' , views.CategoryListApiView.as_view() , name='category_list_api'),
    path('product/detail/<str:prdoct_slug>/' , views.ProductDetailApiView.as_view() , name='product_detail_api'),
    path('bucket/' , views.BucketListApiView.as_view() , name='bucket_api'),
    path('bucket/delete/' , views.BucketDeleteApiView.as_view() , name='bucket_delete_api'),
    path('bucket/download/' , views.BucketDownloadApiView.as_view() , name='bucket_download_api'),
    path('comment/create/',views.CommentCreateApiView.as_view() , name='comment_create_api'),
    path('reply/create/<int:comment_id>/',views.CommentReplyApiView.as_view() , name='reply_create_api'),
    path('comment/list/<slug:product_slug>/',views.CommentListApiView.as_view() , name='comment_list_api'),

]