from django.contrib import admin
from article.models import Article

# Register your models here.
# 装饰器方法注册，推荐
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','is_deleted','readNum','author','creatTime','lastUpdateTime')
    ordering = ("pk",)

