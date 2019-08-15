from django.contrib import admin
from .models import User

admin.site.site_header = 'CSDN微课后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 显示用户的id，账号，用户名，金额，性别， 电话
    list_display = ['id', 'account', 'username', 'money', 'gender', 'tel']
    # 过滤器 按照性别搜索
    list_filter = ['gender', ]
    # 搜索功能按照 用户名，账号
    search_fields = ['account', 'username ']
