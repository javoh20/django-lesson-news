from django.db import models
from django.utils import timezone

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

    class Meta:
        ordering = ['-published_time']
        verbose_name = "News"
        verbose_name_plural = "News"
    
    def __str__(self):
        return self.title