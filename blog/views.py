from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all().order_by('-date_publication')
    paginator = Paginator(articles, 5)  # 5 articles par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"page_obj": page_obj})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "blog/article_detail.html", {"article": article})
