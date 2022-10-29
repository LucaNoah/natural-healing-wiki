from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Article


class ArticleList(generic.ListView):
  model = Article
  queryset = Article.objects.filter(approved=True).order_by('-created_date')
  template_name = 'article_list.html'


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(approved=True)
        article = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
            },
        )


class UserArticles(generic.ListView):
  model = Article
  template_name = 'article_list.html'

  def get_queryset(self):
    return Article.objects.filter(author=self.request.user).order_by('-created_date')


def home_view(request):
    return render(request, 'index.html')


def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('article_title')
        slug = title.replace(' ', '-').lower()
        author = request.user
        description = request.POST.get('article_description')
        content = request.POST.get('article_content')
        Article.objects.create(title=title, slug=slug, author=author, description=description, content=content)

        return redirect('all_articles')
    return render(request, 'create_article.html')


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.title = request.POST.get('article_title')
        article.slug = article.title.replace(' ', '-').lower()
        article.description = request.POST.get('article_description')
        article.content = request.POST.get('article_content')
        article.save()
        return redirect('all_articles')

    return render(request, 'edit_article.html', {
                "article": article,
            },)


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('all_articles')
