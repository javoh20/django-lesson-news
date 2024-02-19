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
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news' : news,
        'categories' : categories,
    }

    return render(request, 'index.html', context)


def NotFoundView(request):
    return render(request,'404.html') 


# def ContactUsView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("Success")

#     context = {
#         'form' : form,
#     }

#     return render(request, 'contact.html', context)


class ContactUsView(TemplateView):
    template_name = 'contact.html'
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        
        context = {
            'form' : form,
        }

        return render(request, 'contact.html', context)
    
    def post(self,request):
        form = ContactForm(request.POST)

        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("Success")
        
        context = {
            'form' : form,
        }

        return render(request, 'contact.html', context)