"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include , re_path
from django.conf.urls.static import static
from django.conf import settings
from home import views
from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


admin.site.site_header = "Book Center Admin"
admin.site.site_title = "Book Center Admin Portal"
admin.site.index_title = "Welcome to Book Center Admin Portal"



schema_view = get_schema_view(
   openapi.Info(
      title="Book Center API",
      default_version='v1.0.0',
      description="this is a book center apis",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rezaamin8889@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('change_language/' , views.ChangeLanguageView.as_view() , name='change_language'),
    # path('admin/', admin.site.urls),
    # path('' , include('home.urls' , namespace='home')),
    # path('accounts/' , include('accounts.urls' , namespace='accounts')),
    # path('orders/' , include('orders.urls' , namespace='orders')),
    path('api/auth/' , include('djoser.urls')),
    path('api/auth/',include('djoser.urls.authtoken')),
    path('api/v1/' , include('api.urls' , namespace='api')),

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('' , include('home.urls' , namespace='home')),
    path('accounts/' , include('accounts.urls' , namespace='accounts')),
    path('orders/' , include('orders.urls' , namespace='orders')),

)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)