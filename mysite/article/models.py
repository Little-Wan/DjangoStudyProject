from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    DoesNotExist = None
    objects = None #先声明
    title = models.CharField(max_length=30)
    content = models.TextField()
    creatTime = models.DateTimeField(auto_now_add=True)
    lastUpdateTime = models.DateTimeField(auto_now=True)
    # 删除数据时对该字段的操作（on_delete）
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    #逻辑删除(对需要删除的数据做标记，勿正式从数据库删除，方便数据回溯)
    is_deleted = models.BooleanField(default=False)
    readNum = models.IntegerField(default=0)

    def __str__(self):
        return self.title

