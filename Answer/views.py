from django.shortcuts import render, HttpResponse
from mywebsocket import consumers
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# 步骤
r = 0
print('R:', r)
test_r = 0
print('test_R:', test_r)
# 服务器地址
# hosts = 'http://192.168.4.121:8080/detao-oa'
hosts0 = 'https://test-oa.xinlianpu.com'
hosts1 = 'http://192.168.4.121:8080/detao-oa'

# 开幕

kaimu_url = '/mobile/amqa/round/qa/direct/foreshow'
# 开始本轮答题
action_round_url = '/mobile/amqa/round/qa/direct/round/begin'
# 开题
kaiti_url = '/mobile/amqa/round/qa/direct/testing/begin'
# 公布答案
gongbudaan_url = '/mobile/amqa/round/qa/direct/testing/end'
# 结束本轮答题
end_round_url = '/mobile/amqa/round/qa/direct/round/end'
# 闭幕
bimu_url = '/mobile/amqa/round/qa/direct/finale'
# 状态
state_url = '/mobile/amqa/round/qa/state'
# 重置
reset_url = '/mobile/amqa/round/qa/direct/reset'
# 获取某场次结果
get_roundret_url = '/mobile/amqa/round/qa/direct/round/result'

api_dict = {
    'kaimu_url': kaimu_url,
    'action_round_url': action_round_url,
    'kaiti_url': kaiti_url,
    'gongbudaan_url': gongbudaan_url,
    'end_round_url': end_round_url,
    'bimu_url': bimu_url,
    'reset_url': reset_url,
    'get_roundret_url': get_roundret_url,
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

@csrf_exempt
def ajax(request):
    global r
    global api_dict
    print('ajax')
    print('POST:', request.POST)
    reset = request.POST.get('reset')
    host = request.POST.get('host')
    print('host', host)
    if host == '1':
        print('测试服务器')
        this_host = hosts1
    else:
        print('正式服务器')
        this_host = hosts0

    if reset:
        reset = int(reset)
        r = reset
        if reset == 999:
            r = 0
            ret0 = requests.post(url=this_host + api_dict.get('reset_url'), data={})
            print('重置结果：-----》', ret0.text)
        print('R:', r)
        return HttpResponse(r)
    api = request.POST.get('api')
    api_real = this_host + api_dict.get(api)
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
        if api == 'gongbudaan_url' or api == 'kaiti_url' or api == 'get_roundret_url':
            d = ret0.json().get('data')
            if d:
                r = r + 1
                print('R:', r)
                if api == 'kaiti_url':
                    answers, title = d.get('answers'), d.get('title')
                    ret_html = '''
                    <p>题目：{}</p>
                    <div class="0 alert" role="alert alert-info">A：{}</div>
                    <div class="1 alert" role="alert alert-info">B：{}</div>
                    <div class="2 alert" role="alert alert-info">C：{}</div>
                    '''.format(title, answers[0], answers[1], answers[2])
                elif api == 'get_roundret_url':
                    dddd = {"round": {
                        "bonusAmount": 2000, "id": 151747643566410000, "playNumber": 0,
                        "startTime": "10:02"},
                        "winners": []}
                    zongshu = 50
                    winners = d.get('winners')
                    ret = []
                    for i in winners:
                        print()
                        print(i.get('wxAvatarUrl'))
                        ret.append({
                            'wxNickname': i.get('wxNickname'),
                            'wxAvatarUrl': i.get('wxAvatarUrl'),
                        })
                    ret_html = json.dumps(ret)
                    print(ret_html)
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

ret = {"code": 0,
       "data": {"round": {"bonusAmount": 2000, "id": 151747643566410000, "playNumber": 0, "startTime": ""},
                "winners": [{"id": 151817140400710295,
                             "wxAvatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLjcVoo3kWxewm8GMRyicKVChj8k9Wt7kJKO1lnVUDX25P4Ic8WvMd4J0xf8USwzNcibed3hj7iatstA/0",
                             "wxNickname": "范斯特罗夫斯基",
                             "wxOpenId": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLjcVoo3kWxewm8GMRyicKVChj8k9Wt7kJKO1lnVUDX25P4Ic8WvMd4J0xf8USwzNcibed3hj7iatstA/0"}]},
       "message": "成功"}
