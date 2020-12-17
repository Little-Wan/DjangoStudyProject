from django.db import models

# Create your models here.
class Article(models.Model):
    DoesNotExist = None
    objects = None #先声明
    title = models.CharField(max_length=30)
    content = models.TextField()

