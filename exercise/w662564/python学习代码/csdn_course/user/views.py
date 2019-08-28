from django.shortcuts import render, HttpResponse, redirect, reverse
from user.models import User
from course import views as course_views
from course.models import Course
from user import views


# Create your views here.
def index_handler(request):
    # 修改资料处理视图
    context = request.context
    session_user = request.session['session_user']
    user = User.objects.get(id=session_user.get('id'))
    context['user'] = user
    if request.method == 'GET':
        return render(request, 'user.html', context)
    else:
        user.username = request.POST.get('username')
        user.gender = request.POST.get('gender')
        user.tel = request.POST.get('tel')
        user.save()
        return redirect(reverse('user_index'))


def course_handler(request):
    # 用户已经已购买的课程
    context = request.context
    session_user = request.session['session_user']
    course_s = User.objects.get(id=session_user.get('id')).userBuyer_set.all()
    context['course_s'] = course_s
    return render(request, 'user_course.html', context)


def Shoppingcart_handler(request):
    # 购物车结构视图
    context = request.context
    session_user = request.session['session_user']
    course_s = User.objects.get(id=session_user.get('id')).userShoppingcart_set.all()
    context['course_s'] = course_s
    return render(request, 'user_shoppingcart.html', context)


def login_handler(request):
    # 登录视图
    if request.method != 'POST':
        return HttpResponse(status=403)
    context = request.context
    account = request.POST.get('account')
    password = request.POST.get('password')
    user_s = User.objects.filter(account=account, password=password)
    if user_s:
        user = user_s[0]
        request.session['session_user'] = {'id': user.id, 'account': user.account}
        return redirect(reverse('course_index'))
    else:
        context['login_message'] = '账号或密码错误'
    return course_views.index_handler(request)


def register_handler(request):
    # 注册处理视图
    if request.method != 'POST':
        return HttpResponse(status=403)
    context = request.context
    account = request.POST.get('account')
    password = request.POST.get('password')
    try:
        user_exists = User.objects.filter(account=account).exists()
        if not user_exists:
            user = User(account=account, password=password)
            user.save()
            request.session['session_user'] = {'id': user.id, 'account': user.account}
        else:
            context['register_message'] = '账号已存在'
    except:
        context['register_message'] = '服务器异常'
    finally:
        return course_views.index_handler(request)


def logout_handler(request):
    # 注销处理视图
    request.session['session_user'] = None
    return redirect(reverse('course_index'))


def purchase_handler(request, course_id):
    # 购买课程视图
    context = request.context
    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session['session_user']
        user = User.objects.get(id=session_user.get('id'))
        if user.money >= course.price:
            user.userBuyer_set.add(course)
            user.money -= course.price
            user.userShoppingcart_set.remove(course)
            user.save()
            context['message'] = '购买成功'

        else:
            context['message'] = '余额不足'
    except:
        context['message'] = '购买失败'
    finally:

        return render(request, 'user_message.html', context)


def addShoppingcart_handler(request, course_id):
    # 加入购物车视图
    context = request.context
    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session['session_user']
        user = User.objects.get(id=session_user.get('id'))
        user.userShoppingcart_set.add(course)
        user.save()
        context['message'] = '添加购物车成功'
    except:
        context['message'] = '添加购物车失败'
    return render(request, 'user_message.html', context)


def redirect_handler(request):
    if request.session == 404:
        return reverse('course_index')
