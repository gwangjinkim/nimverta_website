from django.db import models
from django.utils import timezone

class Page(models.Model):
    title = models.CharField(max_length=200)
    # The slug is the unique URL identifier, e.g., "about", "science"
    slug = models.SlugField(unique=True, help_text="A unique URL-friendly identifier for the page.")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="A unique URL-friendly identifier for the article.")
    content = models.TextField()
    # This is a key field for news!
    publication_date = models.DateTimeField(default=timezone.now) 

class Meta:
    # This ensures the articles are always sorted with the newest first
    ordering = ['- publication_date']

    def __str__(self):
        return self.title
