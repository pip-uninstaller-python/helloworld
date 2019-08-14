# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 20:04
# @Author  : 錵滊嫣缘
# @File    : urls.py
# @Software: PyCharm

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 20:04
# @Author  : 錵滊嫣缘
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_handler, name='user_index'),  # 用户主页
    path('course', views.course_handler, name='user_course'),  # 用户已经已购买的课程
    path('Shoppingcart', views.Shoppingcart_handler, name='user_Shoppingcart'),  # 用户已经加入购物车的课程
    path('login', views.login_handler, name='user_login'),  # 登录
    path('register', views.register_handler, name='user_register'),  # 注册
    path('logout', views.logout_handler, name='user_logout'),  # 注销
    re_path('purchase/(.+)', views.purchase_handler, name='user_purchase'),  # 购买课程
    re_path('addShoppingcart/(.+)', views.addShoppingcart_handler, name='user_addShoppingcart'),  # 加入购物车
    path('redirect',views.redirect_handler),
]
