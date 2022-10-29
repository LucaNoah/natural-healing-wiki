from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wiki_article"
    )
    description = models.TextField(max_length=300)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return f"Written{self.body} by {self.name}"
