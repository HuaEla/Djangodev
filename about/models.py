from django.db import models

# Create your models here.
class homeInner(models.Model):
    h1=models.CharField('一级标题',max_length=100)
    h2=models.CharField('二级标题',max_length=100)

    class Meta:
        verbose_name="主页标题"


class message(models.Model):
    name=models.CharField('姓名',max_length=20)
    phone=models.CharField('电话',max_length=20)
    text=models.TextField('内容')
    create_time=models.DateField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name="留言板"