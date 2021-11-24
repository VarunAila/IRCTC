"""irctc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from train.views import index,showtrains,login,register,logout,forgot,change,book,search,cancel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index , name='index'),
    path('showtrains/', showtrains,name='showtrains'),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path("logout/",logout, name="logout"),
    path('forgot/',forgot,name="forgot"),
    path('change/',change,name='change'),
    path('book/',book,name='book'),
    path('search/',search,name='search'),
    path('cancel/',cancel,name='cancel')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
