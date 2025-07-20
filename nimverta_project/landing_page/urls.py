# landing_page/urls.py

from django.urls import path
from . import views  # The '.' here means 'from the current app directory'

urlpatterns = [
    path('', views.home, name='home'),
    # This new pattern will match urls like /about-us/ or /science/
    # and send the 'slug' to the page_detail view.
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
