from django.contrib import admin

from .models import Article,Comment 

# Register your models here.

# admin.site.register(Article) # admin panelinde göstermek için yaparız..

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):


    list_display = ["title","author","created_date"] # article kısmında gösterilen başlıklardır.
    
    list_display_links = ["title","created_date"] # yazılara link ekliyor

    search_fields = ["title"] # başlığa göre aratma kısmı 

    list_filter = ["created_date"]
    class Meta:
        model = Article # ArticleAdmin ile Article yi birleştirdik


