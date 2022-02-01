from enum import unique
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

from django.contrib import messages

from django.contrib.auth.models import User 
# Create your models here.



class Article(models.Model): # article modeli oluşturmayı deniycez 
    # kaçtane alan olacaksa bunları girmemiz gerekiyor.
                               #  başka bir tabloyu referans ettik
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE , verbose_name= " Yazar ") # bu alan aslında user tablosuna işaretle # o tablonun user ı buraya gelecek
                                                                        # eğer user silinirse user a ait herşey silinecek

    title = models.CharField(max_length=50,verbose_name="Başlık" )  # max uzunluğu 50 olacakk    
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi") # tarihi otomatik alması gerek                                                                
                                         # verbose_name = yazıyı türkçe karşılığını yazarsın
    article_image = models.FileField(blank = True , null = True,verbose_name="Makaleye Fotoğraf Ekleyiniz..")   

    
    def __str__(self):
        return self.title     


    class Meta: 
        ordering = ['-created_date'] # en son eklediğimiz makale ilk gösterilmiş olacak


class Comment(models.Model):

    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")

    # bağlantıyı kurduk

    comment_author = models.CharField(max_length = 50,verbose_name="isim") # {{request.user.username}} request.user
    comment_content = models.CharField(max_length=200,verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    # yorumu oluşturduk

    def __str__(self):
        return self.comment_content

    class Meta:   
        ordering = ['-comment_date']











