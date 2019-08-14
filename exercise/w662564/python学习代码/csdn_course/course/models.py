from django.db import models
from user.models import User
import datetime
import os


# Create your models here.
def save_file(instance, filename):
    return os.path.join('video', filename)


def save_img(instance, filename):
    return os.path.join('static', 'img', filename)


# 课程种类表
class Category(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '课程种类表'

    name = models.CharField(max_length=50, unique=True, verbose_name='课程种类')

    # 定义一个显示的方法
    def __str__(self):
        return self.name


# 课程表：
class Course(models.Model):
    STATUS_CHOICES = (
        (0, '收费'),
        (1, '免费')
    )

    class Meta():
        verbose_name = verbose_name_plural = '课程表'

    courseName = models.CharField(max_length=40, verbose_name='课程名称')
    fileName = models.FileField(upload_to=save_file, verbose_name='文件名称')
    imgname = models.ImageField(upload_to=save_img, verbose_name='课程图片')
    pCategory = models.ForeignKey(to=Category, related_name='courses_set', on_delete=models.CASCADE,
                                  verbose_name='课程类别')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='售价', blank=True)
    summary = models.CharField(max_length=1000, default='', verbose_name='课程介绍', blank=True)
    status = models.PositiveSmallIntegerField(default=0, verbose_name='状态', blank=True,
                                              choices=STATUS_CHOICES)  # 0：收费 1：免费，默认0
    createDatetime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间', blank=True)
    userBuyer = models.ManyToManyField(to=User, related_name='userBuyer_set', verbose_name='购买用户', blank=True)
    userShoppingcart = models.ManyToManyField(to=User, related_name='userShoppingcart_set', verbose_name='加入购物车的用户',
                                              blank=True)
