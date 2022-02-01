from django import forms            #  ***
from .models import Article         ### bunları bir araya getirmiş oluyoruz *** Article formdan bir form oluşturduk 
class ArticleForm(forms.ModelForm): ### ***
    class Meta:                     #   ***
        model = Article             # ****
                                    #    *** 
        fields = ["title","content","article_image"] #     *** dedik ki Article formundan sadece title ve content için bir form yap dedik  #ve article_image kısmını

