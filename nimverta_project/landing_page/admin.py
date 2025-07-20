from django.contrib import admin
from .models import Page, NewsArticle

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')
    # This will automatically pre-fill the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publication_date')
    prepopulated_fields = {'slug': ('title',)}
