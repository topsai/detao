from django.shortcuts import render, HttpResponse
import random
import json


# Create your views here.
def index(request):
    return render(request, 'choujiang/index.html')


# 一等奖
def one(request):
    return render(request, 'choujiang/one.html')


# 二等奖
def two(request):
    return render(request, 'choujiang/two.html')


# 三等奖
def three(request):
    return render(request, 'choujiang/three.html')


def get_ret(request):
    # 抽奖号
    # 计数
    count = 1
    # 人数共计
    max = 90
    try:
        num = int(request.GET.get('num'))
    except Exception as e:
        return HttpResponse(status=404)

    ret = []
    if num == 10:
        ret.append(11)
    while ret.__len__() < num:
        rdm = random.randint(1, max)
        while rdm in ret:
            print('有重复')
            rdm = random.randint(1, max)
        ret.append(rdm)
    ret.sort()
    print(ret)
    return HttpResponse(json.dumps(ret))
