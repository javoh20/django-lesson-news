from .models import News

def latest_news(request):
    news = News.published.all().order_by("-published_time")[:15]

    context = {
        'latest_news' : news,
    }

    return context
