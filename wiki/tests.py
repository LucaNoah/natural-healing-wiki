from django.test import TestCase
from django.test import Client


# tests views.py
class HomeViewTestCase(TestCase):
    def setUp(self):
      pass

    def test_load_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ArticleListTestCase(TestCase):
    def setUp(self):
      pass

    def test_load_view(self):
        c = Client()
        response = c.get('/articles-list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_list.html')


# class ArticleDetailTestCase(TestCase):
#     def setUp(self):
#       pass

#     def test_load_view(self):
#         c = Client()
#         response = c.get('<slug:slug>')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'article_detail.html')


# class UserArticlesTestCase(TestCase):
#     def setUp(self):
#       pass

#     def test_load_view(self):
#         c = Client()
#         response = c.get('/user-articles')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'article_list.html')


class CreateArticleTestCase(TestCase):
    def setUp(self):
      pass

    def test_load_view(self):
        c = Client()
        response = c.get('/create-new-article')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_article.html')


# class EditArticleTestCase(TestCase):
#     def setUp(self):
#       pass

#     def test_load_view(self):
#         c = Client()
#         response = c.get('/edit/<article_id>')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'edit_article.html')


# class DeleteArticleTestCase(TestCase):
#     def setUp(self):
#       pass

#     def test_load_view(self):
#         c = Client()
#         response = c.get('/delete/<article_id>')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'create_article.html')