import re
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404 , reverse
from .forms import ArticleForm
from .models import Article , Comment

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

from django.contrib import messages # django mesajları
# Create your views here.
# url geldiğinde çalışacak fonksiyon yaz.

def articles(request):

    keyword = request.GET.get("keyword")

    if keyword: #araam tuşuna basıldıysa  
        articles = Article.objects.filter(title__contains = keyword)
                    # keywordün geçtiği article döndürecek
                    
        return render(request,"articles.html",{"articles":articles})


    # bütün makaleleri bi listeye atmak istiyoruz
    articles = Article.objects.all() # bütün mamakelleri bu listeye atıcak

    return render(request,"articles.html",{"articles" : articles})






def index(request):

    
    carousels = Article.objects.all()
    return render(request,"index.html",{"carousels":carousels})
    
    return render(request,"index.html")                  # article/index.html HttpResponse("Anasayfa") # veya Anasayfa yaz direk " " içinde


def about(request):
    return render(request,"about.html") 

def detail(request,id):
    return HttpResponse("Detail:" + str(id))

@login_required(login_url = "user:login") # eğer giriş yapmadıysak userın altındaki ismi login olana git diyoruz

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    
    context = {
        "articles":articles
    }

    return render(request , "dashboard.html" , context)

@login_required(login_url = "user:login")
def addarticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)
                                                #resim yüklendiyse file gelicek fakat yoksa fotoğraf None gelicek buraya
    if form.is_valid(): # sıkıntı çıkmadıysa

        article = form.save(commit=False) # yazdığı bilgileri saveledi / sen uğraşma ben yapıcam kayıt işlemini
        """
        article objesi oluşturdu / article.save yapıyor aslında  
        """

        
        article.author = request.user ######################           aradığın yer olabilir
        article.save()
        
        messages.success(request , "Makale Başarıyla Oluşturuldu ...")

        return redirect("index")


    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id) # ilk hangi modelden veri çekeceğini yaz

    comments = article.comments.all()


    return render(request,"detail.html",{"article":article,"comments":comments})





@login_required(login_url = "user:login")

def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)

    form = ArticleForm(request.POST or None , request.FILES or None,instance = article) 
                 # post olursa  verileri yenileriyle güncelliycek                #gönderdiğmiz bilgiler gerekli yerlere yazılacak tır# güncellenmemiş halini al ve yerlere koy
    if form.is_valid():

        article = form.save(commit=False) # yazdığı bilgileri saveledi / sen uğraşma ben yapıcam kayıt işlemini               

        article.author = request.user
        article.save()

        messages.success(request , "Makale Başarıyla Güncellendi ... ")

        return redirect("index")

    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")

def deleteArticle(request,id):

    article = get_object_or_404(Article, id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi..")

    return redirect("article:dashboard")




@login_required(login_url = "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id = id )

    if request.method == "POST":
        comment_author = request.user # name i yazıyoruz # isim inputun name i ni
        comment_content = request.POST.get("comment_content") 

        if comment_content :
            söz = ["mal","salak","amq","aq","gerizekalı","https://","http://","31"]
            for söz in comment_content :

                comment_content
            
            messages.success(request,"İçeriği Değiştiriniz Uygunsuz Kelimeler Var Link Kullanmayınız !!! ")

            return redirect(reverse("article:detail",kwargs = {"id":id})) 


        newComment = Comment(comment_author = comment_author , comment_content = comment_content)

        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail",kwargs = {"id":id})) # 1 url ye gidilcek
                            # /articles/detail/15 getiriyor

@login_required(login_url = "user:login")
def mypage(request):

    return render(request , "myaccount.html" )





@login_required(login_url = "user:login")
def updatepassword(request):



    return render(request , "uppassword.html" )







