from django.contrib import admin
from django.urls import path


    # from article.views import index # article klasörü altında index fonksiyonunu al diyoruz

#isim veriyoruz şu uygulamanın içinde şunu kullarak gerçekleştir # redierecet yaparken kullanıcaz
from . import views

app_name = "article"




urlpatterns = [
    # path('create/',views.index , name = "index"), # çalıştırılcak kodları içine yazarız - /admin yaptığında  admin.site.urls e gidiyor
    #article klasörü içinde uygulama belirttik / yarattık

    path('dashboard/',views.dashboard , name = "dashboard"),
    path('addarticle/',views.addarticle , name = "addarticle"),
    path('article/<int:id>',views.detail , name = "detail"),
    path('update/<int:id>',views.updateArticle , name = "update"),
    path('delete/<int:id>',views.deleteArticle , name = "delete"),
    path('',views.articles , name = "articles"),
    path('comment/<int:id>',views.addComment , name = "comment"),
    path('mypage/',views.mypage , name = "mypage"),
    path('updatepassword/',views.updatepassword , name = "updatepassword"),

    
   

   
]