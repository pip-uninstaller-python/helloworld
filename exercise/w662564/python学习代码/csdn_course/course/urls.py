# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 20:04
# @Author  : 錵滊嫣缘
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_handler, name='course_index'),  # 商城主页处理器
    re_path('course/(.+)', views.course_handler, name='course_course'),  # 课程详细页处理器
    re_path('video/(.+)', views.video_handler, name='course_video'),   # 播放详细页
    re_path('videoStream/(.+)', views.videoStream_handler, name='course_videoStream')  #视频流处理器
]
