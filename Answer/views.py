from django.shortcuts import render, HttpResponse
from mywebsocket import consumers
import requests
import json

# 步骤
r = 0
print('R:', r)
test_r = 0
print('test_R:', test_r)
# 服务器地址
# hosts = 'http://192.168.4.121:8080/detao-oa'
hosts = 'https://test-oa.xinlianpu.com'

# 开幕

kaimu_url = '{}/mobile/amqa/round/qa/direct/foreshow'.format(hosts)
# 开始本轮答题
action_round_url = '{}/mobile/amqa/round/qa/direct/round/begin'.format(hosts)
# 开题
kaiti_url = '{}/mobile/amqa/round/qa/direct/testing/begin'.format(hosts)
# 公布答案
gongbudaan_url = '{}/mobile/amqa/round/qa/direct/testing/end'.format(hosts)
# 结束本轮答题
end_round_url = '{}/mobile/amqa/round/qa/direct/round/end'.format(hosts)
# 闭幕
bimu_url = '{}/mobile/amqa/round/qa/direct/finale'.format(hosts)
# 状态
state_url = '{}/mobile/amqa/round/qa/state'.format(hosts)
# 重置
reset_url = '{}/mobile/amqa/round/qa/reset'.format(hosts)


api_dict = {
    'kaimu_url': kaimu_url,
    'action_round_url': action_round_url,
    'kaiti_url': kaiti_url,
    'gongbudaan_url': gongbudaan_url,
    'end_round_url': end_round_url,
    'bimu_url': bimu_url,
}


# Create your views here.

def index(request):
    if request.method == 'POST':
        print(request.POST)
    topic_num = []
    for i in range(12):
        topic_num.append(i)
    round_num = []
    for i in range(5):
        round_num.append(i)
    return render(request, 'index.html', {'topic_num': topic_num, 'round_num': round_num, 'r': r})


def ws(request):
    return render(request, 'ws.html', )


def send_msg(request):
    if request.method == 'POST':
        consumers.send_msg(request.POST.get('msg'))
        return HttpResponse('ok')


def ajax(request):
    global r

    print('ajax')
    print('POST:', request.POST)
    reset = request.POST.get('reset')
    host = request.POST.get('host')
    print('host', host)
    if host == '1':
        print('测试服务器')
        global test_r
        hosts = 'http://192.168.4.121:8080/detao-oa'
        # 开幕
        kaimu_url = '{}/mobile/amqa/round/qa/direct/foreshow'.format(hosts)
        # 开始本轮答题
        action_round_url = '{}/mobile/amqa/round/qa/direct/round/begin'.format(hosts)
        # 开题
        kaiti_url = '{}/mobile/amqa/round/qa/direct/testing/begin'.format(hosts)
        # 公布答案
        gongbudaan_url = '{}/mobile/amqa/round/qa/direct/testing/end'.format(hosts)
        # 结束本轮答题
        end_round_url = '{}/mobile/amqa/round/qa/direct/round/end'.format(hosts)
        # 闭幕
        bimu_url = '{}/mobile/amqa/round/qa/direct/finale'.format(hosts)
        # 状态
        state_url = '{}/mobile/amqa/round/qa/state'.format(hosts)

        api_dict = {
            'kaimu_url': kaimu_url,
            'action_round_url': action_round_url,
            'kaiti_url': kaiti_url,
            'gongbudaan_url': gongbudaan_url,
            'end_round_url': end_round_url,
            'bimu_url': bimu_url,
        }

        if reset:
            reset = int(reset)
            print('重置', reset, type(reset), int(reset))
            test_r = reset
            print('R:', test_r)
            return HttpResponse(test_r)
        api = request.POST.get('api')

        api_real = api_dict.get(api)
        data = request.POST.get('data')
        if not data:
            data = {}

        ret0 = requests.post(url=api_real, data=data)
        print('data:', data)
        print(ret0)
        print('ret:', ret0.text)
        print('api:', api)
        code = ret0.json().get('code')

        if code == 0:
            if api == 'gongbudaan_url' or api == 'kaiti_url':
                d = ret0.json().get('data')
                if d:
                    test_r = test_r + 1
                    print('R:', test_r)
                    if api == 'kaiti_url':
                        answers, title = d.get('answers'), d.get('title')
                        ret_html = '''
                        <p>题目：{}</p>
                        <div class="0 alert" role="alert">A：{}</div>
                        <div class="1 alert" role="alert">B：{}</div>
                        <div class="2 alert" role="alert">C：{}</div>
                        '''.format(title, answers[0], answers[1], answers[2])
                    else:
                        correctAnswer = d.get('qa').get('correctAnswer')
                        ret_html = correctAnswer

                    return HttpResponse(json.dumps({'r': test_r, 'd': ret_html}))
                else:
                    print('err------1')
                    return HttpResponse(status=404)
            else:
                test_r = test_r + 1
                print('test_r:', test_r)
                return HttpResponse(test_r)
        else:
            print('err------2')
            return HttpResponse(status=404)

    else:
        hosts = 'https://test-oa.detaogig.com'
        # 开幕

        kaimu_url = '{}/mobile/amqa/round/qa/direct/foreshow'.format(hosts)
        # 开始本轮答题
        action_round_url = '{}/mobile/amqa/round/qa/direct/round/begin'.format(hosts)
        # 开题
        kaiti_url = '{}/mobile/amqa/round/qa/direct/testing/begin'.format(hosts)
        # 公布答案
        gongbudaan_url = '{}/mobile/amqa/round/qa/direct/testing/end'.format(hosts)
        # 结束本轮答题
        end_round_url = '{}/mobile/amqa/round/qa/direct/round/end'.format(hosts)
        # 闭幕
        bimu_url = '{}/mobile/amqa/round/qa/direct/finale'.format(hosts)
        # 状态
        state_url = '{}/mobile/amqa/round/qa/state'.format(hosts)

        api_dict = {
            'kaimu_url': kaimu_url,
            'action_round_url': action_round_url,
            'kaiti_url': kaiti_url,
            'gongbudaan_url': gongbudaan_url,
            'end_round_url': end_round_url,
            'bimu_url': bimu_url,
        }

        if reset:
            reset = int(reset)
            print('重置', reset, type(reset), int(reset))
            r = reset
            print('R:', r)
            return HttpResponse(r)
        api = request.POST.get('api')

        api_real = api_dict.get(api)
        data = request.POST.get('data')
        if not data:
            data = {}

        ret0 = requests.post(url=api_real, data=data)
        print('data:', data)
        print(ret0)
        print('ret:', ret0.text)
        print('api:', api)
        code = ret0.json().get('code')

        if code == 0:
            if api == 'gongbudaan_url' or api == 'kaiti_url':
                d = ret0.json().get('data')
                if d:
                    r = r + 1
                    print('R:', r)
                    if api == 'kaiti_url':
                        answers, title = d.get('answers'), d.get('title')
                        ret_html = '''
                        <p>题目：{}</p>
                        <div class="0 alert" role="alert">A：{}</div>
                        <div class="1 alert" role="alert">B：{}</div>
                        <div class="2 alert" role="alert">C：{}</div>
                        '''.format(title, answers[0], answers[1], answers[2])
                    else:
                        correctAnswer = d.get('qa').get('correctAnswer')
                        ret_html = correctAnswer

                    return HttpResponse(json.dumps({'r': r, 'd': ret_html}))
                else:
                    print('err------1')
                    return HttpResponse(status=404)
            else:
                r = r + 1
                print('R:', r)
                return HttpResponse(r)
        else:
            print('err------2')
            return HttpResponse(status=404)


# 开题
cc = {"code": 0, "data": {"answers": ["一座岛屿", "一种药物", "一种乐器"], "qaIndex": 0, "title": "座头鲸的‘座头’来源于:"}, "message": "成功"}
# 公布答案
ret = {"code": 0, "data": {"amountAllUser": 2,
                           "answerChoices": [{"amount": 0, "qaIndex": 0}, {"amount": 0, "qaIndex": 1},
                                             {"amount": 2, "qaIndex": 2}],
                           "qa": {
                               "answers": ["一座岛屿", "一种药物", "一种乐器"],
                               "correctAnswer": 2, "qaIndex": 0,
                               "title": "座头鲸的‘座头’来源于:"}, "selection": 2}, "message": "成功"}
# api: gongbudaan_url
