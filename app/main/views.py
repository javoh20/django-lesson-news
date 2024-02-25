from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView

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
    news_list = News.published.all().order_by('-published_time')[:5]
                                                                                                       
    local_news = News.published.filter(category__name = "Local").order_by('-published_time')[:5]
                                                                                                       
    foreign_news = News.published.filter(category__name = "Foreign").order_by('-published_time')[:5]
                                                                                                       
    techno_news = News.published.filter(category__name = "Technology").order_by('-published_time')[:5]
                                                                                                       
    sport_news = News.published.filter(category__name = "Sport").order_by('-published_time')[:5]
                                                                                                       
    categories = Category.objects.all()
    context = {
        "active_nav" : "home",

        'news_list' : news_list,

        'local_news' : local_news,

        'foreign_news' : foreign_news,

        'techno_news' : techno_news,

        'sport_news' : sport_news,

        'categories' : categories,
    }
                                                                                                       
    return render(request, 'index.html', context)


def NotFoundView(request):
    context = {
        "active_nav" : "404",
    }

    return render(request, '404.html', context) 


def ContactUsView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Success")

    context = {
        'form' : form,
        "active_nav" : "contact",
    }

    return render(request, 'contact.html', context)
