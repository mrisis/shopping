from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('register/' , views.UserRegisterView.as_view() , name='user_register'),
    path('register/verify/' , views.UserRegisterVerifyView.as_view() , name='verify_code'),

]