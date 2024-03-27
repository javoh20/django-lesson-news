from django.db import models
from django.utils import timezone
from .managers import *
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    
    title = models.CharField(max_length = 250)
    slug = models.CharField(max_length = 250)
    disc = models.TextField()
    img = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    published_time = models.DateTimeField(default = timezone.now)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 2, choices = Status.choices, default = Status.Draft)

    published = PublishedManager()

    class Meta:
        ordering = ['-published_time']
        verbose_name = "News"
        verbose_name_plural = "News"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Addvertising(models.Model):
    name = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'news/images')
    url = models.URLField()


    def __str__(self):    
        return self.name
    
    class Meta:
        verbose_name = 'Add Banner'
        verbose_name_plural = 'Add Banner'

class SiteSocial(models.Model):
    facebook = models.URLField(verbose_name="Facebook")
    twitter = models.URLField(verbose_name="Twitter")
    dots = models.URLField(verbose_name="dots")
    pinterest = models.URLField(verbose_name="Pinterest")
    google_plus = models.URLField(verbose_name="Google+")
    v = models.URLField(verbose_name="V")
    youtube = models.URLField(verbose_name="YouTube")
    mail = models.URLField(verbose_name="Mail")

    def __str__(self):
        return "Social"

class Comment(models.Model):
    news = models.ForeignKey(News,
                             on_delete = models.CASCADE,
                             related_name = 'comments')
    user = models.ForeignKey(User, 
                             on_delete = models.CASCADE,
                             related_name = 'comments')
    
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']
    
    def __str__(self):
        return f"Comment - {self.body}, - by {self.user}"
    
