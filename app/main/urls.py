from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name = "home"),
    path('404/', NotFoundView, name = 'not_found'),
    path('contact/', ContactUsView, name = 'contact'),
    
    path('all/', news_list, name = "all_news_list"),
    path('news/<slug:news>', news_detail, name = "news_detail_page"),
    
    path('local/', LocalNewsView.as_view(), name = "Local"),
    path('foreign/', ForeignNewsView.as_view(), name = "Foreign"),
    path('science/', ScienceNewsView.as_view(), name = "Science"),
    path('sport/', SportNewsView.as_view(), name = "Sport"),
    path('techno/', TechnoNewsView.as_view(), name = "Technology"),

    path('news/<slug:slug>/edit/', NewsEditView.as_view(), name = "news_edit"),
    path('news/<slug:slug>/delete/', NewsDeleteView.as_view(), name = "news_delete"),
    path('news/create/', NewsCreateView.as_view(), name = "news_create"),

]
