from django.test import TestCase
from django.test import Client


# tests views.py
class HomeViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get(" / ")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class ArticleListTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/articles-list")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "article_list.html")