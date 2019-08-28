from django.contrib import admin
from .models import Course, Category


# Register your models here.
@admin.register(Category)
# 注册种类模型类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    # 模糊查询功能
    search_fields = ['name']


@admin.register(Course)
# 注册课程表模型类
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['userBuyer', 'userShoppingcart']
    # 展示字段 id, 课程名称，售价，简介，状态，创建的时间
    list_display = ['id', 'courseName', 'price', 'summary', 'status', 'createDatetime']
    # 过滤器 根据创建时间，状态来过滤
    list_filter = ['status', 'createDatetime']
    # 模糊搜索 支持名称搜索，支持价格搜索
    search_fields = ['courseName', 'price']
