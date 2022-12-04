from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('register/' , views.UserRegisterView.as_view() , name='user_register'),
    path('register/verify/' , views.UserRegisterVerifyView.as_view() , name='verify_code'),
    path('logout/' , views.UserLogout.as_view() , name='user_logout'),
    path('login/' , views.UserLoginView.as_view() , name='user_login'),

]