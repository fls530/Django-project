from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登陆操作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect("/event_manage/")
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            # 讲session记录到浏览器
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
def event_manage(request):
    # 读取浏览器cookie
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {'user': username})
