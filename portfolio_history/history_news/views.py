from django.shortcuts import render

# Create your views here.
from .models import Article

def latest_news(request):
    articles = Article.objects.all().order_by('-publish_date')[:5]
    return render(request, 'latest_news.html', {'articles': articles})
