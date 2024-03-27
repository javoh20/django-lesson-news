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
admin.site.register(Addvertising)
admin.site.register(SiteSocial)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comment', "active_comment"]

    def disable_comment(self, queryset):
        queryset.update(active = False)

    def active_comment(self, queryset):
        queryset.update(active = True)