from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'disc']


# admin.site.register(News)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']

admin.site.register(Contact)
admin.site.register(Add)
admin.site.register(SiteSocial)