from django.shortcuts import render, HttpResponse
import random
import json

# 人数共计
max = 90
lotters = []
for i in range(1, max):
    lotters.append(i)
all_lotters = []


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
    try:
        num = int(request.GET.get('num'))
    except Exception as e:
        return HttpResponse(status=404)
    # 本次获奖
    ret = []
    while ret.__len__() < num:
        rdm = lotters.pop()
        ret.append(rdm)
    ret.sort()
    all_lotters.extend(ret)
    all_lotters.sort()
    print(ret)
    print('all:', all_lotters)
    return HttpResponse(json.dumps(ret))
