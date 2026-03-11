from django.contrib import admin
from .models import Categorie, Projet, ContentBlock

class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 1

class ProjetAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie")
    inlines = [ContentBlockInline]

admin.site.register(Categorie)
admin.site.register(Projet, ProjetAdmin)
