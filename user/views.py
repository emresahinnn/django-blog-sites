import string
from django.shortcuts import render,redirect #anasayfaya url gitmeye yarıyor 
from . forms import LoginForm, RegisterForm , forms 

from django.db import models
from enum import unique

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages # django mesajları
from django.contrib.auth.models import User      #  yap

from django.contrib.auth import login,authenticate,logout         # aynı zamanda giriş yapılamsını istiyorsan burasını yaz # authenticate  böyle bir kullanıcı olup olmadığına bakıyor

# Create your views here.

def register(request):
                        # eğer get request olduysa boşmuş gibi gelecek / eğer post request se request.POST  olarak gelcek
    form = RegisterForm(request.POST or None )

    if form.is_valid(): # django gidiyor clean methodu çağırıyor  
                            # formdan aldığı değerler yanlışsa false dönüyor // uyarı fırlatıyor.

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        

        newUser = User(username = username , email = email )
        newUser.set_password(password)

        

        messages.info(request,"Başarıyla Kayıt Oldunuz...")


        ###

        username = request.POST["username"]
        email = request.POST["email"]

        subject = 'YB Blog Account Security'
        message = f""" Hİ

          An Account Has Been Created For This Email With The Name ' {username} ' .
        ---------------------------------------------------------------------------
        ACCOUNT INFO :  User name : {username} , Password : {password}
        ---------------------------------------------------------------------------
        """
        from_email = settings.EMAIL_HOST_USER
        recipent_list = [email]

        send_mail(subject ,message , from_email , recipent_list , fail_silently=False)


        newUser.save() # kullanıcı kaydedildi
        login(request,newUser)

    
        return redirect("index")
        

    context = {
        "form":form
    }
    return render(request,"register.html",context)

    
    
######################

def loginUser(request):

    if request.user.is_authenticated:

        messages.success(request," Şuanda Giriş Yapılmış Bir Hesaptasınız ! ")

        return redirect("index")
    else:

        form = LoginForm(request.POST or None )

        context = {
        "form" : form
        }

        # post request kontrol etmek 

        if form.is_valid(): #eğer true ise 

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username , password = password)

            if user is None : #böyle bir kullanıcı yoksa 
                messages.info(request,"Kullanıcı Adı veya Parola Hatalı...")

                return render(request,"login.html",context)

            
            messages.success(request,"Başarıyla Giriş Yaptınız ... ")

            login(request,user) # sisteme giriş yapmasını sağladık

            #anasayfaya dönmemiz gerekiyor

            return  redirect("index")


        return render(request,"login.html",context)


    #####################3
    
def logoutUser(request):   #### ***********

    if request.user.is_authenticated == False:

        messages.success(request,"Çıkış Yapmak İçin Giriş Yapınız !")

        return redirect("index")

    else:        ### ************

        logout(request)

        messages.success(request,"Başarıyla Çıkış Yaptınız .. ")

        return redirect("index")









