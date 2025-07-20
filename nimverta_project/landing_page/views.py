from django.shortcuts import render, get_object_or_404
from .models import Page

def home(request):
    # This tells Django to render the 'home.html' template
    return render(request, 'home.html')

def page_detail(request, slug):
    # 1. Get the specific page object from the database using the slug from the URL.
    # 2. If a page with that slug doesn't exist, it will automatically show a "404 Not Found" error.
    page = get_object_or_404(Page, slug=slug)
    
    # 3. Pass the found 'page' object into the template.
    context = {
        'page': page
    }
    
    # 4. Render the page_detail.html template with the page's data.
    return render(request, 'page_detail.html', context)
