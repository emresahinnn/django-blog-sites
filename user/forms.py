from enum import unique
from django import forms 
from django.forms.fields import CharField

from django.contrib.auth.models import User 

from django.db import models

class LoginForm(forms.Form):

    username = forms.CharField(label="kullanıcı Adı ")
    password = forms.CharField(label="Parola",widget = forms.PasswordInput)
    #confirm = forms.CharField(label = "Parola Doğrula ",widget = forms.PasswordInput)






class RegisterForm(forms.Form): 

    
    
    

    username = forms.CharField( max_length= 50 , label = "Kullanıcı Adı" )
    password = forms.CharField(max_length=20 , label = "Parola",widget = forms.PasswordInput ) # normal bir şifre girilin yer gibi gözükecek
    confirm = forms.CharField(max_length=20 , label = "Parola Doğrula",widget = forms.PasswordInput)
    email = forms.CharField(max_length=30 , label = "Gmail adresi" )

    


    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("bu Email Kullanılıyor Başka Email Yazınız!!")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("bu Kullanıcı Adı Kullanılıyor Başka Bir Ad Yazınız!!")

        elif email.endswith("@gmail.com" or " @yahoo.com") == False  :

            raise forms.ValidationError("gmail gerçek değildir")    

        elif email.endswith("@gmail.com" or " @yahoo.com") == True  :
            

            if password and confirm and password != confirm : # EĞER ikisi girilmişse ve aynı değilse 
                raise forms.ValidationError("Parolalar eşleşmiyor")

            values = {
                "username" : username ,
                "password" : password , 
                "email":email,
            
            }
            return values

        

        # password ile confirm alanının uyuştuğunu kontrol etmesi için bi fonksiyon var django da

        # if email.endswith("@gmail.com" or " @yahoo.com") == False  :

            # raise forms.ValidationError("gmail gerçek değildir")    

        # elif email.endswith("@gmail.com" or " @yahoo.com") == True  :
            

            # if password and confirm and password != confirm : # EĞER ikisi girilmişse ve aynı değilse 
                # raise forms.ValidationError("Parolalar eşleşmiyor")

            # elif User.objects.filter(email=email).exists():
                # raise ValidationError("Email already exists")
            

            
            
            #eğer password ve confirm aynı ise bu /
            


        

            values = {
                "username" : username ,
                "password" : password , 
                "email":email,
            
            }
            return values



    
