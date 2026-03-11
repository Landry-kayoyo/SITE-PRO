from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)  # image principale
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100, default="Landry")

    def __str__(self):
        return self.titre


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/albums/")
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image de {self.article.titre}"
