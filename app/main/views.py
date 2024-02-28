from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView


# Create your views here.
def news_list(request):
    news_list = News.published.all()

    context = {
        "news_list" : news_list,
    }

    return render(request, "list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug = news, status = News.Status.Published)
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

class LocalNewsView(ListView):
    model = News
    template_name = 'category/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = "Local")
        return news
    
class ForeignNewsView(ListView):
    model = News
    template_name = 'category/foreign.html'
    context_object_name = 'foreign_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = "Foreign")
        return news
    
class ScienceNewsView(ListView):
    model = News
    template_name = 'category/science.html'
    context_object_name = 'science_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = "Science")
        return news
    
class SportNewsView(ListView):
    model = News
    template_name = 'category/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = "Sport")
        return news
    
class TechnoNewsView(ListView):
    model = News
    template_name = 'category/technology.html'
    context_object_name = 'techno_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = "Technology")
        return news