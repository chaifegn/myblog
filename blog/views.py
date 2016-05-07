# -*- coding:utf-8 -*-

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })
def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'post.html',{'post':post})

def hello(request):
    # -----使用list
    my_list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # -----使用dictionary
    dict = {'天氣': '晴', '溫度': '21', '濕度': '70%'}
    # -----使用dictionary更新內容與合併list
    dict2 = {}
    first_names = ["三", "四"]
    last_names = ["張", "李"]
    first_names.append("五")
    last_names.append("王")
    for name in zip(last_names, first_names):
        dict2.update({name})
    # -----
    my_list2 = map(int, range(1, 101))
    # -----
    return render(request, 'hello.html',
                  {'current_time': datetime.now(),
                   'list': my_list,
                   'list2': my_list2,
                   'dict': dict,
                   'dict2': dict2
                   })


def copyfile(request):
    return render(request, 'copy.html')


def add(request):
    # 輸入的網址http://127.0.0.1:8000/add/?a=44&b=55
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    ans = '{0} + {1} = {2}'.format(a, b, str(c))
    return HttpResponse(ans)


def add2(request, a, b):
    # 原本傳入的a跟b都是String
    # 所以要轉成int才能做運算
    # 輸入的網址http://127.0.0.1:8000/add2/45/50/
    c = int(a) + int(b)
    ans = '{0} + {1} = {2}'.format(a, b, str(c))
    return HttpResponse(ans)
