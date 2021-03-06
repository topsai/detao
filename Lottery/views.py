from django.shortcuts import render, HttpResponse
import random
import json
import logging

logger = logging.getLogger('detao')

# 人数共计
max = 90
lotters = []
# 排除
excspt = [10]
exc = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def action():
    print('action')
    lotters.clear()
    print(lotters)
    for i in range(1, max + 1):
        lotters.append(i)

    lotters.pop(10)
    random.shuffle(lotters)


action()
print('lotters:---', lotters)


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
    logger.debug('---reset---')
    logger.info('---reset---info')
    logger.warning('waring------')
    logger.error('err-----')
    try:
        num = int(request.GET.get('num'))
    except Exception as e:
        reset = request.GET.get('reset')
        if reset:

            print('reset')
            action()
            print('new_lotters:----', lotters)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    ret = []
    if num == 1:
        pass
    if num == 10:
        pass
    if num == 30:
        ret.append(11)
        pass

    if ret.__len__() + lotters.__len__() < num:
        print('未中奖人数不够了')
        return HttpResponse(status=505)
    # 本次获奖
    while ret.__len__() < num:
        rdm = lotters.pop()
        if rdm in exc:
            continue
        ret.append(rdm)
    ret.sort()
    print(ret)
    print('未中奖：', lotters, lotters.__len__())
    random.shuffle(lotters)
    return HttpResponse(json.dumps(ret))
