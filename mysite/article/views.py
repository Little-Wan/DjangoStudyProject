from django.shortcuts import render
from django.http import HttpResponse,Http404
from article.models import Article

# Create your views here.
def article_detail(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("not exist")
    return HttpResponse("<h2>文章标题： %s</h2><br>文章内容：%s"%(article.title,article.content))