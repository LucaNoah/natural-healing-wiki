from . import views
from wiki.views import create_article
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('create_new_article', create_article, name='add_article'),
]