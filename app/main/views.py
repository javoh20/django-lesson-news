from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def news_list(request):
    news_list = News.published.all()

    context = {
        "news_list" : news_list,
    }

    return render(request, "list.html", context)

def news_detail(request, id):
    news = get_object_or_404(News, id = id, status = News.Status.Published)
    context = {
        "news": news
    }

    return render(request, "detail.html", context)

def HomeView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news' : news,
        'categories' : categories,
    }

    return render(request, 'index.html', context)

def NotFoundView(request):
    return render(request,'404.html') 

def ContactUsView(request):
    context = {
        # 'form' : form,
    }
    return render(request, 'contact.html', context)