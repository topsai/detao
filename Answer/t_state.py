#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/2/7


import requests
import threading
import json
import time

# hosts = 'https://test-oa.detaogig.com'
hosts = 'https://test-oa.xinlianpu.com'
state_url = '{}/mobile/amqa/round/qa/loop'.format(hosts)

print(state_url)
count_err = 0


def action(i):
    global count_err
    # test_state = {
    #     'wxOpenId': 'asfasfasf{}'.format(i),
    #     'wxNickname': 'asfsafasf{}'.format(i),
    # }

    data = \
        {
            "wxNickName": "毛委员",
            "wxAvatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83epibMzuxCCR243iaL8AJtLz0byO6Xs2MMc7OywjvHp692axI8psREps7zSjZiaWIMI4pAxoRtiamYeGjQ/0",
            "wxOpenId": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83epibMzuxCCR243iaL8AJtLz0byO6Xs2MMc7OywjvHp692axI8psREps7zSjZiaWIMI4pAxoRtiamYeGjQ/0",
        }
    try:
        ret = requests.post(url=state_url, data=json.dumps(data))
        # print(ret.text)
        if ret.json().get('code') != 0:
            count_err += 1
    except Exception as e:
        print(e)


while True:
    for i in range(1000):
        t = threading.Thread(target=action, args=(i,))
        t.start()
    time.sleep(1)
    print('错误次数：', count_err)
