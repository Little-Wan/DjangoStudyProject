from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from article.models import Article

# Create your views here.
def article_detail(request,article_id):
    # 原始方法
    # try:
    #     article = Article.objects.get(id=article_id)
    #     context ={}
    #     # 将article对象作为值传递给contex参数，context参数为字典格式
    #     context["article_obj"] = article
    #     # return render(request,"article_detail.html",context)
    #     return render_to_response("article_detail.html", context)
    # except Article.DoesNotExist:
    #     raise Http404("not exist")
    # # return HttpResponse("<h2>文章标题： %s</h2><br>文章内容：%s"%(article.title,article.content))

    #内置方法
    article = get_object_or_404(Article,pk=article_id)
    context = {}
    # 将article对象作为值传递给contex参数，context参数为字典格式
    context["article_obj"] = article
    return render_to_response("article_detail.html", context)

def article_list(request):
    # 筛选固定字段显示
    articles = Article.objects.filter(is_deleted=False)
    context = {}
    context["articles"] = articles
    return render_to_response("article_list.html",context)