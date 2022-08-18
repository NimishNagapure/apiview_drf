from django.db import models

# Create your models here.

class Author(models.Model):
    name =models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    body = models.CharField(max_length=300)
    author = models.ForeignKey('Author',related_name='articles',on_delete=models.CASCADE)

    def __str__(self):
        return self.title