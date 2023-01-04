
from django.urls import path
from .import views

urlpatterns = [
    

    path('',views.home,name="home"),
    path('news/search',views.search_news,name="search-news"),
    path('news/sources',views.sources,name="sources")
]
