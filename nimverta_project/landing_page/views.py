from django.shortcuts import render

def home(request):
    # This tells Django to render the 'home.html' template
    return render(request, 'home.html')
