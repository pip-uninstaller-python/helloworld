import os

from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Course, Category
from user.models import User
from django.http import StreamingHttpResponse


# Create your views here.
def index_handler(request):
    # 商城主页信息处理
    context = request.context
    category_s = Category.objects.all()
    course_data_s = []
    for category in category_s:
        course_data_s.append(
            {
                'category': category.name,
                'course_s': category.courses_set.all()
            }
        )
    context['course_data_s'] = course_data_s
    return render(request, 'index.html', context)


def course_handler(request, course_id):
    # 课程详细页
    context = request.context
    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session.get('session_user', None)
        if session_user:
            context['view_perssion'] = User.objects.filter(id=session_user.get('id'),
                                                           userBuyer_set__id=course.id).exists()
        context['course'] = course
        return render(request, 'course.html', context)
    except:
        return HttpResponse(status=404)


def video_handler(request, course_id):
    # 立即播放视图
    context = request.context
    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session['session_user']
        boolean_buyed = User.objects.filter(id=session_user.get('id'), userBuyer_set__id=course_id).exists()
        if boolean_buyed:
            context['course'] = course
            return render(request, 'video.html', context)
        else:
            return redirect(reverse('course_course', args=(course.id,)))
    except:
        return HttpResponse(status=404)


def videoStream_handler(request, course_id):
    # 视频播放视图
    def read_video(path):
        with open(path, 'rb') as f:
            while True:
                data = f.read(10 * 1024)
                if data:
                    yield data
                else:
                    break

    context = request.context
    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session['session_user']
        boolean_buyed = User.objects.filter(id=session_user.get('id'), userBuyer_set__id=course_id).exists()
        if boolean_buyed:
            context['course'] = course
            response = StreamingHttpResponse(read_video(course.fileName.__str__()), status=206)  # 206 是视频的传输状态码
            bytes_max = 1024 * 1024 * 2  # 2M
            response['Content-Range'] = 'bytes 0-%s/%s' % (bytes_max, os.path.getsize(course.fileName.__str__()))
            # response['Content-Range'] = 'bytes 0-10240/%s' % os.path.getsize(course.fileName.__str__())
            return response
        else:
            return redirect(reverse('course_course', args=(course.id,)))
    except:
        return HttpResponse(status=404)
