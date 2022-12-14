from django.urls import path
from . import views



app_name = 'api'
urlpatterns = [
    path('users_list/', views.UserListAPIView.as_view(), name='users_list'),
    ]