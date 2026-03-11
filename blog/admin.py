from django.contrib import admin
from .models import Article, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "date_publication")
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
