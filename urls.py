from django.urls import path
from news.views import scrape, news_list, news_detail, category_news_list, search_news

urlpatterns = [
    # Path for scraping news based on a specific name
    path('scrape/<str:name>/', scrape, name="scrape"),

    # Path for displaying the list of news
    path('', news_list, name="home"),

    # Path for viewing details of a specific news article
    path('news/<int:pk>/', news_detail, name="news_detail"),

    # Path for displaying news based on a specific category
    path('category/<str:category>/', category_news_list, name="category_news"),

    # Path for searching news articles
    path('search/', search_news, name="search_news"),
]
