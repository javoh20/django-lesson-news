from django.db import models
from django.utils import timezone
from .managers import *
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
    published_time = models.DateTimeField(timezone.now)
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

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Add(models.Model):
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
    