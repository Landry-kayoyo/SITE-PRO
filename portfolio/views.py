from django.shortcuts import render, get_object_or_404
from .models import Projet, Categorie

def portfolio_list(request):
    categories = Categorie.objects.all()
    return render(request, "portfolio/portfolio_list.html", {"categories": categories})

def portfolio_detail(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, "portfolio/portfolio_detail.html", {"projet": projet})
