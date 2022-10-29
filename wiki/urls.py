from . import views
from wiki.views import create_article, home_view, edit_article
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('articles-list', views.ArticleList.as_view(), name='all_articles'),
    path('user-articles', views.UserArticles.as_view(), name='user_articles'),
    path('create-new-article', views.create_article, name='add_article'),
    path('edit/<article_id>', views.edit_article, name='update_article'),
    path('delete/<article_id>', views.delete_article, name='delete_article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
]