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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home import views
from django.conf.urls.i18n import i18n_patterns


admin.site.site_header = "Book Center Admin"
admin.site.site_title = "Book Center Admin Portal"
admin.site.index_title = "Welcome to Book Center Admin Portal"


urlpatterns = [
    path('change_language/' , views.ChangeLanguageView.as_view() , name='change_language'),
    # path('admin/', admin.site.urls),
    # path('' , include('home.urls' , namespace='home')),
    # path('accounts/' , include('accounts.urls' , namespace='accounts')),
    # path('orders/' , include('orders.urls' , namespace='orders')),
    path('api/v1/' , include('api.urls' , namespace='api')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('' , include('home.urls' , namespace='home')),
    path('accounts/' , include('accounts.urls' , namespace='accounts')),
    path('orders/' , include('orders.urls' , namespace='orders')),

)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)