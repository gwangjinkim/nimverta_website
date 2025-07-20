# landing_page/urls.py

from django.urls import path
from . import views  # The '.' here means 'from the current app directory'

urlpatterns = [
    # When the URL passed from the main urls.py is empty (''),
    # run the 'home' function from our views.py file.
    path('', views.home, name='home'),
]
