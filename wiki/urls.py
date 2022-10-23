from . import views
from wiki.views import create_article, home_view, edit_article
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
    path('articles_list', views.ArticleList.as_view(), name='all_articles'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('create_new_article', create_article, name='add_article'),
    path('edit/<article_id>', edit_article, name='update_article')
]