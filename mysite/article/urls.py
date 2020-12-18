from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/article/
    path('', views.article_list,name = "article_list"),
    # http://127.0.0.1:8000/article/1
    path('<int:article_id>', views.article_detail,name = "article_detail"),
]