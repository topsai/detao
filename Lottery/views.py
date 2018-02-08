from django.shortcuts import render, HttpResponse
import random
import json


# Create your views here.
def index(request):
    return render(request, 'choujiang/index.html')


def one(request):
    return render(request, 'choujiang/one.html')


def two(request):
    return render(request, 'choujiang/two.html')


def get_ret(request):
    # 抽奖号
    count = 90
    try:
        num = int(request.GET.get('num'))
    except:
        pass
    if num in [1, 10, 30]:
        ret = []
        for i in range(int(num)):
            rdm = random.randint(1, count)
            while rdm in ret:
                print('有重复')
                rdm = random.randint(1, count)
            ret.append(rdm)
        ret.sort()
        print(ret)
        return HttpResponse(json.dumps(ret))
    else:
        print('no')
