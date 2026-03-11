from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    categorie = models.ForeignKey(Categorie, related_name='projets', on_delete=models.CASCADE)
    lien = models.URLField(blank=True, null=True)  # Lien externe (GitHub, démo...)
    date_creation = models.DateTimeField(auto_now_add=True)  # ✅ nouveau champ
    
    def __str__(self):
        return self.titre


class ContentBlock(models.Model):
    TYPE_CHOICES = [
        ('titre', 'Titre'),
        ('sous_titre', 'Sous-titre'),
        ('texte', 'Texte'),
        ('image', 'Image'),

    ]
    projet = models.ForeignKey(Projet, related_name='blocks', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    contenu = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/blocks/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.projet.titre} - {self.type}"
