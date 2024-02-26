from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name = "home"),
    path('404/', NotFoundView, name = 'not_found'),
    path('contact/', ContactUsView, name = 'contact'),
    path('all/', news_list, name = "all_news_list"),
    path('news/<slug:news>', news_detail, name = "news_detail_page"),
    path('local/', LocalNewsView.as_view(), name = "local_news"),
]
