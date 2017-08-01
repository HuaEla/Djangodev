from django.db import models

# Create your models here.

class homeInner(models.Model):
    h1=models.CharField('一级标题',max_length=100)
    h2=models.CharField('二级标题',max_length=100)

    class Meta:
        verbose_name="主页标题"

class coder(models.Model):
    img=models.CharField('照片',max_length=100)
    name=models.CharField('姓名',max_length=100)
    motto=models.CharField('格言',max_length=100)
    class Meta:
        verbose_name=('开发团队')
class sales(models.Model):
    img = models.CharField('照片', max_length=100)
    name=models.CharField('姓名',max_length=100)
    motto=models.CharField('格言',max_length=100)
    class Meta:
        verbose_name=("销售团队")
class tech(models.Model):
    img = models.CharField('照片', max_length=100)
    name=models.CharField('姓名',max_length=100)
    motto=models.CharField('格言',max_length=100)
    class Meta:
        verbose_name=("售后团队")