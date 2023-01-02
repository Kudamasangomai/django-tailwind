
from django.urls import path
from .import views

urlpatterns = [
    

    path('',views.home,name="home"),
    path('nes/search',views.search_news,name="search-news")
]
