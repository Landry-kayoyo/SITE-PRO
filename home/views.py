from django.shortcuts import render
from blog.models import Article
from portfolio.models import Projet, Categorie
from django.db.models import Count

def home_view(request):
    # Récupérer les 3 derniers articles du blog
    articles_recents = Article.objects.all().order_by('-date_publication')[:3]
    
    # Récupérer les 3 derniers projets du portfolio
    projets_recents = Projet.objects.all().order_by('-date_creation')[:3]
    
    # Statistiques calculées automatiquement
    projets_count = Projet.objects.count()
    articles_count = Article.objects.count()
    
    # Compter les catégories de projets
    categories_count = Categorie.objects.count()
    
    # Nombre total de blocs de contenu (si utile)
    from portfolio.models import ContentBlock
    total_blocks = ContentBlock.objects.count()
    
    # Statistiques par catégorie de projet
    projets_par_categorie = Categorie.objects.annotate(
        nombre_projets=Count('projets')
    ).order_by('-nombre_projets')[:3]
    
    # Compter les certifications (à adapter si tu as un modèle Certification)
    # Si tu n'as pas encore de modèle, garde une valeur par défaut
    certifications_count = 3  # À remplacer par Certification.objects.count() quand tu auras le modèle
    
    annees_etudes = 3  # Valeur fixe
    
    context = {
        # Données principales
        'articles_recents': articles_recents,
        'projets_recents': projets_recents,
        
        # Statistiques globales
        'projets_count': projets_count,
        'articles_count': articles_count,
        'categories_count': categories_count,
        'certifications_count': certifications_count,
        'annees_etudes': annees_etudes,
        'total_blocks': total_blocks,
        
        # Données additionnelles
        'projets_par_categorie': projets_par_categorie,
        
        # Informations de l'utilisateur
        'nom_complet': 'Landry',
        'universite': 'Université Don Bosco de Lubumbashi',
        'ville': 'Lubumbashi',
        'pays': 'RDC',
    }
    
    return render(request, 'home/home.html', context)