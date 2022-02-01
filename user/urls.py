from django.contrib import admin
from django.urls import path

    # from article.views import index # article klasörü altında index fonksiyonunu al diyoruz

#isim veriyoruz şu uygulamanın içinde şunu kullarak gerçekleştir # redierecet yaparken kullanıcaz
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register , name = "register"), 
    path('login/',views.loginUser , name = "login"), 
    path('logout/',views.logoutUser , name = "logout"), 

   ##
    
    

]













