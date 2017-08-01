from django.db import models

# Create your models here.


class homeInner(models.Model):
    h1=models.CharField('一级标题',max_length=100)
    h2=models.CharField('二级标题',max_length=100)

    class Meta:
        verbose_name = ('主页标题')

class hire(models.Model):
    position=models.CharField('职位',max_length=100)
    welfare=models.CharField('福利',max_length=100)
    salary=models.CharField('薪资',max_length=100)
    requirements=models.CharField('要求',max_length=100)

    class Meta:
        verbose_name=('招聘')
