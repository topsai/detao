#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/1/30


import requests
import json


# hosts = 'http://192.168.4.121:8080/detao-oa'

# get = 'https://test-oa.detaogig.com/mobile/amqa/round/qa/get'
# get = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/get'
# add = 'https://test-oa.detaogig.com/mobile/amqa/round/qa/add'



# 控制开幕
#  /mobile/amqa/round/qa/direct/foreshow
#  控制本场开始
#  /round/qa/direct/round/begin
#  {
#     'round':0
#  }
#  控制答题开始
#  /mobile/amqa/round/qa/direct/testing/begin
#  {
#     'round':0,
#     'qaIndex':0
#  }
#  控制答题答案公布
#  /mobile/amqa/round/qa/direct/testing/end
#  {
#     'round':0,
#     'questionId':12342323234234
#  }
#  控制本场开奖
#  /mobile/amqa/round/qa/direct/round/end
#  {
#     'round':0
#  }
#  控制闭幕
#  /mobile/amqa/round/qa/direct/finale


# data = json.dumps(data)
# ret = requests.post(url=add, data=data)
# print(ret.text)
# print(ret)
# add = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/add'
# action0 = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/direct/foreshow'
# action1 = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/direct/round/begin'
# # 开题
# action2 = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/direct/testing/begin'
# # 公布答案
# action3 = 'http://192.168.4.121:8080/detao-oa/mobile/amqa/round/qa/direct/testing/end'
#
# d0 = {
#     'round': 0,
# }
#
# d1 = {
#     'round': 0,
#     'qaIndex': 0
# }
#
# #
# ret0 = requests.post(url=action0, data=json.dumps({}))
# ret1 = requests.post(url=action1, data=json.dumps(d0))
# ret2 = requests.post(url=action2, data=json.dumps(d1))
#
# import time
# print(ret0)
# print(ret0.text)
# time.sleep(3)
# print('------')
# print(ret1)
# print(ret1.text)
# time.sleep(3)
# print('------')
# print(ret2)
# print(ret2.text)

# # 添加数据
# ret = requests.post(url=add, data=json.dumps(data))
# print(ret)
# print(ret.text)
add = 'https://test-oa.xinlianpu.com/mobile/amqa/round/qa/add'
for i in range(5):
    print(i)
    data = {
        'round': i,
        'bonusAmount': 300+i,
        'qas': [
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿一座岛屿一座岛屿', '一种药物', '一种乐器'], 'correctAnswer': 0},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物*', '一种乐器'], 'correctAnswer': 1},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物', '一种乐器*'], 'correctAnswer': 2},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿*', '一种药物', '一种乐器'], 'correctAnswer': 0},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物*', '一种乐器'], 'correctAnswer': 1},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物', '一种乐器*'], 'correctAnswer': 2},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿*', '一种药物', '一种乐器'], 'correctAnswer': 0},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物*', '一种乐器'], 'correctAnswer': 1},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物', '一种乐器*'], 'correctAnswer': 2},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿*', '一种药物', '一种乐器'], 'correctAnswer': 0},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物*', '一种乐器'], 'correctAnswer': 1},
            {'title': '座头鲸的‘座头’来源于:', 'answers': ['一座岛屿', '一种药物', '一种乐器*'], 'correctAnswer': 2},

        ]
    }
    ret = requests.post(url=add, data=json.dumps(data))
    print(ret)
    print(ret.text)
