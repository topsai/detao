#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2018/2/11

import requests
import json

data = [
    {
        'round': 0,
        'bonusAmount': 300,
        'qas': [
            {'title': '以下哪种水果是热带水果？', 'answers': ['苹果', '桃子', '香蕉'], 'correctAnswer': 2},
            {'title': '我国共有几个直辖市？', 'answers': ['3', '4', '5'], 'correctAnswer': 1},
            {'title': '德稻全球创新网络的英文简称是什么？', 'answers': ['GIN', 'GIG', 'CIN'], 'correctAnswer': 0},
            {'title': '《孔乙己》的作者是哪位？', 'answers': ['鲁迅', '老舍', '郭沫若'], 'correctAnswer': 0},
            {'title': '花甲之年指的是多少岁', 'answers': ['50岁', '60岁', '70岁'], 'correctAnswer': 1},
            {'title': '以下哪个岛屿是泰国的？', 'answers': ['沙巴', '苏梅岛', '长滩岛'], 'correctAnswer': 1},
            {'title': '下列哪句是李白的诗句？', 'answers': ['竹外桃花三两枝', '葡萄美酒夜光杯', '孤帆远影碧空尽'],
             'correctAnswer': 2},
            {'title': '湖南省因位于哪个湖以南而得名？', 'answers': ['洞庭湖', '鄱阳湖', '镜泊湖'], 'correctAnswer': 0},
            {'title': '动漫《哆啦A梦》中，哆啦A梦的身体最初是什么颜色?', 'answers': ['蓝色', '黄色', '白色'], 'correctAnswer': 1},
            {'title': '下列哪一部不是李安导演的作品？', 'answers': ['风月', '少年派的奇幻漂流', '断背山'], 'correctAnswer': 0},
            {'title': '“中庸之道”是哪个流派的理论？', 'answers': ['儒家', '道家', '法家'], 'correctAnswer': 0},
            {'title': '下列哪一项不属于声音的特性？', 'answers': ['声速', '响度', '音调'], 'correctAnswer': 0},
        ]
    },

    {
        'round': 1,
        'bonusAmount': 400,
        'qas': [
            {'title': '煮熟的鸡蛋清是什么颜色', 'answers': ['白色', '黄色', '透明色'], 'correctAnswer': 0},
            {'title': '“但愿人长久，千里共婵娟”是哪位作家的作品？', 'answers': ['苏轼', '苏辙', '苏洵'], 'correctAnswer': 0},
            {'title': '<<西游记>>中的火焰山在今天的', 'answers': ['陕西', '青海', '新疆'], 'correctAnswer': 2},
            {'title': ' 一公斤铁和一公斤棉花哪一个轻?', 'answers': ['一样重', '棉花', '铁'], 'correctAnswer': 0},
            {'title': '涮羊肉起源于', 'answers': ['宋朝', '元朝', '清朝'], 'correctAnswer': 1},
            {'title': '张继科是什么项目运动员？', 'answers': ['羽毛球', '足球', '乒乓球'], 'correctAnswer': 2},
            {'title': '以下哪个景点不在北京？', 'answers': ['天坛', '兵马俑', '长城'], 'correctAnswer': 1},
            {'title': '电影《刘三姐》是反映-什么民族的生活故事?', 'answers': ['苗族', '侗族', '壮族'], 'correctAnswer': 2},
            {'title': '我司大师众多，请问，以下哪位大师是女性：', 'answers': ['马宁格', '温可馨', '李若云'], 'correctAnswer': 0},
            {'title': '康熙皇帝的庙号是', 'answers': ['太祖', '圣祖', '世祖'], 'correctAnswer': 1},
            {'title': '人体消化道中最长的器官是', 'answers': ['大肠', '小肠', '十二指肠'], 'correctAnswer': 1},
            {'title': '以下哪种蛇是有毒的：', 'answers': ['银环蛇', '玉斑锦蛇', '黑头蟒'], 'correctAnswer': 0},

        ]
    },
    {
        'round': 2,
        'bonusAmount': 500,
        'qas': [
            {'title': '北京奥运会是哪一年举办?', 'answers': ['2004', '2008', '2012'], 'correctAnswer': 1},
            {'title': '"天生我材必有用，千金散尽还复来"出自哪首诗?', 'answers': ['《饮中八仙歌》', '《将进酒》', '《致酒行》'], 'correctAnswer': 1},
            {'title': '长篇小说《骆驼祥子》的作者是以下哪位?', 'answers': ['老舍', '巴金', '矛盾'], 'correctAnswer': 0},
            {'title': '“打蛇打七寸”中七寸是指蛇的？', 'answers': ['心脏', '脑袋', '肾脏'], 'correctAnswer': 0},
            {'title': '以下哪座城市不是德国的城市：', 'answers': ['柏林', '法兰克福', '布鲁塞尔'], 'correctAnswer': 2},
            {'title': '校园歌曲《童年》的词曲作者是：', 'answers': ['罗大佑', '李宗盛', '高晓松'], 'correctAnswer': 0},
            {'title': '李白笔下的"飞流直下三千尺，疑是银河落九天"指的是哪个风景区?', 'answers': ['黄山', '庐山', '华山'], 'correctAnswer': 1},
            {'title': '我国模特界外号是“大表姐”的是哪位模特？', 'answers': ['刘雯', '吕燕', '奚梦瑶'], 'correctAnswer': 0},
            {'title': '七大洲中面积第二的是?', 'answers': ['非洲', '欧洲', '亚洲'], 'correctAnswer': 0},
            {'title': '"豆寇年华"是指几岁?', 'answers': ['13岁', '14岁', '15岁'], 'correctAnswer': 0},
            {'title': '人们常说:"无事不登三宝殿"你知道"三宝"是指哪三宝?', 'answers': ['纸、砚、笔', '书、剑、琴 ', '佛、法、僧'], 'correctAnswer': 2},
            {'title': '以下哪个建筑不是由我司渡堂海大师参与设计的：', 'answers': ['张家界大峡谷玻璃桥', '上海世博会以色列馆', '蒙巴纳斯大厦'], 'correctAnswer': 2},

        ]
    },
    {
        'round': 3,
        'bonusAmount': 500,
        'qas': [
            {'title': '以下哪种产品不能带上火车：', 'answers': ['汽油', '白酒', '中药'], 'correctAnswer': 0},
            {'title': '以上哪个车标没有动物', 'answers': ['标志', '捷豹', '路虎'], 'correctAnswer': 2},
            {'title': '以下哪个成语不可以用来形容夫妻', 'answers': ['相敬如宾', '狼狈为奸', '举案齐眉'], 'correctAnswer': 1},
            {'title': '“八小时工作制度”最早是在哪个国家出现的？', 'answers': ['法国', '中国', '英国'], 'correctAnswer': 2},
            {'title': '老挝的首都是哪里？', 'answers': ['万象', '河内', '胡志明市'], 'correctAnswer': 0},
            {'title': '“黔”是哪个省的简称？', 'answers': ['甘肃', '云南', '贵州'], 'correctAnswer': 2},
            {'title': '“我就是我，是颜色不一样的烟火”是哪首歌？', 'answers': ['《烟火》', '《我》', '《红》'], 'correctAnswer': 1},
            {'title': '豌豆黄属于哪个地区的传统小吃？', 'answers': ['上海', '北京', '成都'], 'correctAnswer': 1},
            {'title': '世界上最大的古代土石建筑工程是哪一个?', 'answers': ['中国的万里长城', '埃及的金字塔', '古罗马的斗兽场'], 'correctAnswer': 0},
            {'title': '以下哪个国家的圣诞节正逢夏季?', 'answers': ['加拿大', '新西兰', '瑞士'], 'correctAnswer': 1},
            {'title': '寒月是指农历几月：', 'answers': ['10月', '11月', '12月'], 'correctAnswer': 0},
            {'title': '我司艾斯林格大师是哪国国籍', 'answers': ['德国', '丹麦', '美国'], 'correctAnswer': 2},

        ]
    },
    {
        'round': 4,
        'bonusAmount': 500,
        'qas': [
            {'title': '螃蟹有几条腿：', 'answers': ['6', '8', '10'], 'correctAnswer': 1},
            {'title': '英文字母表s后面的字母是？', 'answers': ['t', 'r', 'u'], 'correctAnswer': 0},
            {'title': '国粹是指什么艺术形式？', 'answers': ['京剧', '越剧', '相声'], 'correctAnswer': 0},
            {'title': '歇后语“老虎屁股”下一句是？', 'answers': ['打不得', '摸不得', '摸不到'], 'correctAnswer': 1},
            {'title': '徐悲鸿擅长画什么动物？', 'answers': ['虾', '虎', '马'], 'correctAnswer': 2},
            {'title': '植树节是为了纪念谁？', 'answers': ['孙中山', '周恩来', '胡适'], 'correctAnswer': 0},
            {'title': '骆驼的驼峰是储存什么的？', 'answers': ['水', '脂肪', '食物'], 'correctAnswer': 1},
            {'title': '办公自动化简称是？', 'answers': ['OA', 'CL', 'OB'], 'correctAnswer': 0},
            {'title': '文景之治出现在哪个朝代？', 'answers': ['汉', '唐', '宋'], 'correctAnswer': 0},
            {'title': '德稻沙河办公区座机是多少', 'answers': ['70603333', '60703333', '66773333'], 'correctAnswer': 1},
            {'title': '下列元素，空气中含量最多的是？', 'answers': ['氧', '氮', '二氧化碳'], 'correctAnswer': 1},
            {'title': '“德稻”多少笔画？', 'answers': ['28', '29', '30'], 'correctAnswer': 2},
        ]
    },
]

add = 'https://test-oa.xinlianpu.com/mobile/amqa/round/qa/add'
for i in data:
    ret = requests.post(url=add, data=json.dumps(i))
    print(ret)
    print(ret.text)
