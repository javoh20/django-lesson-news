from .models import *

def latest_news(request):
    news = News.published.all().order_by("-published_time")[:15]

    context = {
        'latest_news' : news,
    }

    return context

def AddBanner(request):
    add = Addvertising.objects.last()

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

def AllCategories(request):
    category = Category.objects.all()

    context = {
        'all_categories' : category,
    }

    return context