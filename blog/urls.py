"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static



    # from article.views import index # article klasörü altında index fonksiyonunu al diyoruz

from article import views

urlpatterns = [
    path('admin/', admin.site.urls), # çalıştırılcak kodları içine yazarız - /admin yaptığında  admin.site.urls e gidiyor
    path('', views.index,name="index"), # "" olucak  / " " değil :)
    path('about/', views.about,name="about"),
        #path('detail/<int:id>', views.detail,name="detail"),
    path('articles/',include("article.urls")), # articles kalıbını gördükten sonra article.urls e bak ve daha sorna bu dosyada arama işlemi gerçekleştir
    path('user/',include("user.urls")), # user/register  // user/login // user/logout  bu halde tanımlamış olduk
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

