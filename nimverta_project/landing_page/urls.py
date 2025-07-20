# landing_page/urls.py

from django.urls import path
from . import views  # The '.' here means 'from the current app directory'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
