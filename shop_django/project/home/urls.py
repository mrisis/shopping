from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    path('bucket/' , views.BucketHome.as_view() , name='bucket'),
    path('delete/obj/bucket/<str:key>/' , views.DeleteBucketObject.as_view() , name='delete_obj_bucket'),
    path('download/obj/bucket/<str:key>/' , views.DownloadBucketObject.as_view() , name='download_obj_bucket'),
    path('',views.HomeView.as_view(),name='home'),
    path('menu/',views.MenuView.as_view(), name='menu'),
    path('detail/<int:product_id>/<slug:slug>/', views.ProductDetailView.as_view() , name='product_detail'),
    path('category/<slug:slug_cateory>/' , views.MenuView.as_view(),name='category_filter'),
    path('replay/<int:product_id>/<int:comment_id>/' , views.ProductAddReplayView.as_view(),name='add_replay'),

]