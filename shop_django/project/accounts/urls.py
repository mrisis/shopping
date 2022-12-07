from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('register/' , views.UserRegisterView.as_view() , name='user_register'),
    path('register/verify/' , views.UserRegisterVerifyView.as_view() , name='verify_code'),
    path('logout/' , views.UserLogout.as_view() , name='user_logout'),
    path('login/' , views.UserLoginView.as_view() , name='user_login'),
    path('profile/<int:user_id>/' , views.UserProfileView.as_view() , name='user_profile'),
    path('rest/' , views.UserPasswordResetView.as_view() , name='rest_password'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]