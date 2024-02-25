from .models import *

def latest_news(request):
    news = News.published.all().order_by("-published_time")[:15]

    context = {
        'latest_news' : news,
    }

    return context

def AddBanner(request):
    add = Add.objects.last()

    context = {
        'add_banner' : add,
    }

    return context

def Social(request):
    social = SiteSocial.objects.last()

    context = {
        'social' : social,
    }

    return context