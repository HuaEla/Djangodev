from django.db import models

# Create your models here.



class homeInner(models.Model):
    h1=models.CharField('一级标题',max_length=100)
    h2=models.CharField('二级标题',max_length=100)

    class Meta:
        verbose_name = ('主页标题')

class product(models.Model):
    pro=models.CharField('产品',max_length=50)

    class Meta:
        verbose_name=('产品')


class case(models.Model):
    img=models.CharField('图片',max_length=200)
    title=models.CharField('标题',max_length=200)
    text=models.CharField('内容',max_length=500)

    class Meta:
        verbose_name=('案例')
