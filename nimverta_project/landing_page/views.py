from django.shortcuts import render, get_object_or_404
from .models import Page

def home(request):
    # This tells Django to render the 'home.html' template
    return render(request, 'home.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    context = {'page': page}    
    return render(request, 'page_detail.html', context)

def news_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'news_list.html', {'articles': articles})

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    return render(request, 'news_detail.html', {'article': article})
