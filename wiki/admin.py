from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

  summernote_fields = ('content')
  prepopulated_fields = {'slug': ('title',)}
  list_filter = ('approved', 'created_date', 'author')
  list_display = ('title', 'approved', 'author', 'created_date')
  search_fields = ['title', 'description', 'content']
  actions = ['approve_article']

  def approve_article(self, request, queryset):
    queryset.update(approved=True)
