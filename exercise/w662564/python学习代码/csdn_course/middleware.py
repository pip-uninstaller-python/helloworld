# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 22:59
# @Author  : 錵滊嫣缘
# @File    : middleware.py
# @Software: PyCharm
from django.utils.deprecation import MiddlewareMixin
from course import views as course_views
from django.shortcuts import reverse
import re, re


class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        # 初始化中间件
        print('init_mymiddleware')

    def process_request(self, request):
        request.context = {}
        session_user = None
        # if 'session_user' in request.session.keys():
        #     session_user = request.context['session_user'] = request.session['session_user']
        # if not session_user:
        #     if request.path.startswith('/video') or request.path.startswith('/user'):
        #         if request.path not in [reverse('user_login'),reverse('user_register')]: # 这里是把注册和登录接口让出来
        #             request.context['login_message'] = '请先登录'
        #             return course_views.index_handler(request)
        request.context = dict(
            session_user=request.session['session_user'] if 'session_user' in request.session.keys() else None
        )
        if (not request.context['session_user']) and \
                (request.path.startswith('/video') or request.path.startswith('/user')) and \
                request.path not in [reverse('user_login'), reverse('user_register')]:
            request.context['login_message'] = '请先登录'
            return course_views.index_handler(request)
        # url = re('(^\w+.*\d+')+'index.html'
        # if url==True:
        #     return request('127.0.0.1')


    def process_response(self, request, response):
        # 必须return response
        print('process_response')
        return response
