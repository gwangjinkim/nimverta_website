from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    # The slug is the unique URL identifier, e.g., "about", "science"
    slug = models.SlugField(unique=True, help_text="A unique URL-friendly identifier for the page.")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
