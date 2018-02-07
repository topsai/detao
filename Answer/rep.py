#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/2/6

import re

data = '''

<div class="row">
                <input id="0" class="btn btn-default disabled" type="submit" value="开幕" onclick="kaimu()">
                <div class="">
                    <input id="1" class="btn btn-default disabled" type="submit" value="开始第0轮"
                           onclick="action_round(0)">
                    <div>
                        <div>
                            <input id="2" class="btn btn-default disabled" type="submit" value="开题0"
                                   onclick="kaiti(0, 0)">
                            <input id="3" class="btn btn-default disabled" type="submit" value="公布答案0"
                                   onclick="gongbudaan(0, 0)">
                        </div>
                        <div>
                            <input id="4" class="btn btn-default disabled" type="submit" value="开题1"
                                   onclick="kaiti(0, 1)">
                            <input id="5" class="btn btn-default disabled" type="submit" value="公布答案1"
                                   onclick="gongbudaan(0, 1)">
                        </div>

                        <div>
                            <input id="6" class="btn btn-default disabled" type="submit" value="开题2"
                                   onclick="kaiti(0, 2)">
                            <input id="7" class="btn btn-default disabled" type="submit" value="公布答案2"
                                   onclick="gongbudaan(0, 2)">
                        </div>

                        <div>
                            <input id="8" class="btn btn-default disabled" type="submit" value="开题3"
                                   onclick="kaiti(0, 3)">
                            <input id="9" class="btn btn-default disabled" type="submit" value="公布答案3"
                                   onclick="gongbudaan(0, 3)">
                        </div>

                        <div>
                            <input id="10" class="btn btn-default disabled" type="submit" value="开题4"
                                   onclick="kaiti(0, 4)">
                            <input id="11" class="btn btn-default disabled" type="submit" value="公布答案4"
                                   onclick="gongbudaan(0, 4)">
                        </div>

                        <div>
                            <input id="12" class="btn btn-default disabled" type="submit" value="开题5"
                                   onclick="kaiti(0, 5)">
                            <input id="13" class="btn btn-default disabled" type="submit" value="公布答案5"
                                   onclick="gongbudaan(0, 5)">
                        </div>

                        <div>
                            <input id="14" class="btn btn-default disabled" type="submit" value="开题6"
                                   onclick="kaiti(0, 6)">
                            <input id="15" class="btn btn-default disabled" type="submit" value="公布答案6"
                                   onclick="gongbudaan(0, 6)">
                        </div>

                        <div>
                            <input id="16" class="btn btn-default disabled" type="submit" value="开题7"
                                   onclick="kaiti(0, 7)">
                            <input id="17" class="btn btn-default disabled" type="submit" value="公布答案7"
                                   onclick="gongbudaan(0, 7)">
                        </div>

                        <div>
                            <input id="18" class="btn btn-default disabled" type="submit" value="开题8"
                                   onclick="kaiti(0, 8)">
                            <input id="19" class="btn btn-default disabled" type="submit" value="公布答案8"
                                   onclick="gongbudaan(0, 8)">
                        </div>

                        <div>
                            <input id="20" class="btn btn-default disabled" type="submit" value="开题9"
                                   onclick="kaiti(0, 9)">
                            <input id="21" class="btn btn-default disabled" type="submit" value="公布答案9"
                                   onclick="gongbudaan(0, 9)">
                        </div>

                        <div>
                            <input id="22" class="btn btn-default disabled" type="submit" value="开题10"
                                   onclick="kaiti(0, 10)">
                            <input id="23" class="btn btn-default disabled" type="submit" value="公布答案10"
                                   onclick="gongbudaan(0, 10)">
                        </div>

                        <div>
                            <input id="24" class="btn btn-default disabled" type="submit" value="开题11"
                                   onclick="kaiti(0, 11)">
                            <input id="25" class="btn btn-default disabled" type="submit" value="公布答案11"
                                   onclick="gongbudaan(0, 11)">
                        </div>

                    </div>
                    <input id="26" class="btn btn-default disabled" type="submit" value="结束第0轮" onclick="end_round(0)">

                </div>
                <br><br><br><br>

                <div>

                    <input id="27" class="btn btn-default disabled" type="submit" value="开始第1轮"
                           onclick="action_round(1)">
                    <div>

                        <div>
                            <input id="28" class="btn btn-default disabled" type="submit" value="开题0"
                                   onclick="kaiti(1, 0)">
                            <input id="29" class="btn btn-default disabled" type="submit" value="公布答案0"
                                   onclick="gongbudaan(1, 0)">
                        </div>

                        <div>
                            <input id="30" class="btn btn-default disabled" type="submit" value="开题1"
                                   onclick="kaiti(1, 1)">
                            <input id="31" class="btn btn-default disabled" type="submit" value="公布答案1"
                                   onclick="gongbudaan(1, 1)">
                        </div>

                        <div>
                            <input id="32" class="btn btn-default disabled" type="submit" value="开题2"
                                   onclick="kaiti(1, 2)">
                            <input id="33" class="btn btn-default disabled" type="submit" value="公布答案2"
                                   onclick="gongbudaan(1, 2)">
                        </div>

                        <div>
                            <input id="34" class="btn btn-default disabled" type="submit" value="开题3"
                                   onclick="kaiti(1, 3)">
                            <input id="35" class="btn btn-default disabled" type="submit" value="公布答案3"
                                   onclick="gongbudaan(1, 3)">
                        </div>

                        <div>
                            <input id="36" class="btn btn-default disabled" type="submit" value="开题4"
                                   onclick="kaiti(1, 4)">
                            <input id="37" class="btn btn-default disabled" type="submit" value="公布答案4"
                                   onclick="gongbudaan(1, 4)">
                        </div>

                        <div>
                            <input id="38" class="btn btn-default disabled" type="submit" value="开题5"
                                   onclick="kaiti(1, 5)">
                            <input id="39" class="btn btn-default disabled" type="submit" value="公布答案5"
                                   onclick="gongbudaan(1, 5)">
                        </div>

                        <div>
                            <input id="40" class="btn btn-default disabled" type="submit" value="开题6"
                                   onclick="kaiti(1, 6)">
                            <input id="41" class="btn btn-default disabled" type="submit" value="公布答案6"
                                   onclick="gongbudaan(1, 6)">
                        </div>

                        <div>
                            <input id="42" class="btn btn-default disabled" type="submit" value="开题7"
                                   onclick="kaiti(1, 7)">
                            <input id="43" class="btn btn-default disabled" type="submit" value="公布答案7"
                                   onclick="gongbudaan(1, 7)">
                        </div>

                        <div>
                            <input id="44" class="btn btn-default disabled" type="submit" value="开题8"
                                   onclick="kaiti(1, 8)">
                            <input id="45" class="btn btn-default disabled" type="submit" value="公布答案8"
                                   onclick="gongbudaan(1, 8)">
                        </div>

                        <div>
                            <input id="46" class="btn btn-default disabled" type="submit" value="开题9"
                                   onclick="kaiti(1, 9)">
                            <input id="47" class="btn btn-default disabled" type="submit" value="公布答案9"
                                   onclick="gongbudaan(1, 9)">
                        </div>

                        <div>
                            <input id="48" class="btn btn-default disabled" type="submit" value="开题10"
                                   onclick="kaiti(1, 10)">
                            <input id="49" class="btn btn-default disabled" type="submit" value="公布答案10"
                                   onclick="gongbudaan(1, 10)">
                        </div>

                        <div>
                            <input id="50" class="btn btn-default disabled" type="submit" value="开题11"
                                   onclick="kaiti(1, 11)">
                            <input id="51" class="btn btn-default disabled" type="submit" value="公布答案11"
                                   onclick="gongbudaan(1, 11)">
                        </div>

                    </div>
                    <input id="52" class="btn btn-default disabled" type="submit" value="结束第1轮" onclick="end_round(1)">

                </div>
                <br><br><br><br>

                <div>

                    <input id="53" class="btn btn-default disabled" type="submit" value="开始第2轮"
                           onclick="action_round(2)">
                    <div>

                        <div>
                            <input id="53" class="btn btn-default disabled" type="submit" value="开题0"
                                   onclick="kaiti(2, 0)">
                            <input id="54" class="btn btn-default disabled" type="submit" value="公布答案0"
                                   onclick="gongbudaan(2, 0)">
                        </div>

                        <div>
                            <input id="55" class="btn btn-default disabled" type="submit" value="开题1"
                                   onclick="kaiti(2, 1)">
                            <input id="56" class="btn btn-default disabled" type="submit" value="公布答案1"
                                   onclick="gongbudaan(2, 1)">
                        </div>

                        <div>
                            <input id="57" class="btn btn-default disabled" type="submit" value="开题2"
                                   onclick="kaiti(2, 2)">
                            <input id="58" class="btn btn-default disabled" type="submit" value="公布答案2"
                                   onclick="gongbudaan(2, 2)">
                        </div>

                        <div>
                            <input id="59" class="btn btn-default disabled" type="submit" value="开题3"
                                   onclick="kaiti(2, 3)">
                            <input id="60" class="btn btn-default disabled" type="submit" value="公布答案3"
                                   onclick="gongbudaan(2, 3)">
                        </div>

                        <div>
                            <input id="61" class="btn btn-default disabled" type="submit" value="开题4"
                                   onclick="kaiti(2, 4)">
                            <input id="62" class="btn btn-default disabled" type="submit" value="公布答案4"
                                   onclick="gongbudaan(2, 4)">
                        </div>

                        <div>
                            <input id="63" class="btn btn-default disabled" type="submit" value="开题5"
                                   onclick="kaiti(2, 5)">
                            <input id="64" class="btn btn-default disabled" type="submit" value="公布答案5"
                                   onclick="gongbudaan(2, 5)">
                        </div>

                        <div>
                            <input id="65" class="btn btn-default disabled" type="submit" value="开题6"
                                   onclick="kaiti(2, 6)">
                            <input id="66" class="btn btn-default disabled" type="submit" value="公布答案6"
                                   onclick="gongbudaan(2, 6)">
                        </div>

                        <div>
                            <input id="67" class="btn btn-default disabled" type="submit" value="开题7"
                                   onclick="kaiti(2, 7)">
                            <input id="68" class="btn btn-default disabled" type="submit" value="公布答案7"
                                   onclick="gongbudaan(2, 7)">
                        </div>

                        <div>
                            <input id="69" class="btn btn-default disabled" type="submit" value="开题8"
                                   onclick="kaiti(2, 8)">
                            <input id="70" class="btn btn-default disabled" type="submit" value="公布答案8"
                                   onclick="gongbudaan(2, 8)">
                        </div>

                        <div>
                            <input id="71" class="btn btn-default disabled" type="submit" value="开题9"
                                   onclick="kaiti(2, 9)">
                            <input id="72" class="btn btn-default disabled" type="submit" value="公布答案9"
                                   onclick="gongbudaan(2, 9)">
                        </div>

                        <div>
                            <input id="73" class="btn btn-default disabled" type="submit" value="开题10"
                                   onclick="kaiti(2, 10)">
                            <input id="74" class="btn btn-default disabled" type="submit" value="公布答案10"
                                   onclick="gongbudaan(2, 10)">
                        </div>

                        <div>
                            <input id="75" class="btn btn-default disabled" type="submit" value="开题11"
                                   onclick="kaiti(2, 11)">
                            <input id="76" class="btn btn-default disabled" type="submit" value="公布答案11"
                                   onclick="gongbudaan(2, 11)">
                        </div>

                    </div>
                    <input id="77" class="btn btn-default disabled" type="submit" value="结束第2轮" onclick="end_round(2)">

                </div>
                <br><br><br><br>

                <div>

                    <input id="0" class="btn btn-default disabled" type="submit" value="开始第3轮"
                           onclick="action_round(3)">
                    <div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题0"
                                   onclick="kaiti(3, 0)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案0"
                                   onclick="gongbudaan(3, 0)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题1"
                                   onclick="kaiti(3, 1)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案1"
                                   onclick="gongbudaan(3, 1)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题2"
                                   onclick="kaiti(3, 2)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案2"
                                   onclick="gongbudaan(3, 2)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题3"
                                   onclick="kaiti(3, 3)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案3"
                                   onclick="gongbudaan(3, 3)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题4"
                                   onclick="kaiti(3, 4)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案4"
                                   onclick="gongbudaan(3, 4)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题5"
                                   onclick="kaiti(3, 5)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案5"
                                   onclick="gongbudaan(3, 5)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题6"
                                   onclick="kaiti(3, 6)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案6"
                                   onclick="gongbudaan(3, 6)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题7"
                                   onclick="kaiti(3, 7)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案7"
                                   onclick="gongbudaan(3, 7)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题8"
                                   onclick="kaiti(3, 8)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案8"
                                   onclick="gongbudaan(3, 8)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题9"
                                   onclick="kaiti(3, 9)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案9"
                                   onclick="gongbudaan(3, 9)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题10"
                                   onclick="kaiti(3, 10)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案10"
                                   onclick="gongbudaan(3, 10)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题11"
                                   onclick="kaiti(3, 11)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案11"
                                   onclick="gongbudaan(3, 11)">
                        </div>

                    </div>
                    <input id="0" class="btn btn-default disabled" type="submit" value="结束第3轮" onclick="end_round(3)">

                </div>
                <br><br><br><br>

                <div>

                    <input id="0" class="btn btn-default disabled" type="submit" value="开始第4轮"
                           onclick="action_round(4)">
                    <div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题0"
                                   onclick="kaiti(4, 0)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案0"
                                   onclick="gongbudaan(4, 0)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题1"
                                   onclick="kaiti(4, 1)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案1"
                                   onclick="gongbudaan(4, 1)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题2"
                                   onclick="kaiti(4, 2)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案2"
                                   onclick="gongbudaan(4, 2)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题3"
                                   onclick="kaiti(4, 3)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案3"
                                   onclick="gongbudaan(4, 3)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题4"
                                   onclick="kaiti(4, 4)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案4"
                                   onclick="gongbudaan(4, 4)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题5"
                                   onclick="kaiti(4, 5)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案5"
                                   onclick="gongbudaan(4, 5)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题6"
                                   onclick="kaiti(4, 6)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案6"
                                   onclick="gongbudaan(4, 6)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题7"
                                   onclick="kaiti(4, 7)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案7"
                                   onclick="gongbudaan(4, 7)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题8"
                                   onclick="kaiti(4, 8)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案8"
                                   onclick="gongbudaan(4, 8)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题9"
                                   onclick="kaiti(4, 9)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案9"
                                   onclick="gongbudaan(4, 9)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题10"
                                   onclick="kaiti(4, 10)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案10"
                                   onclick="gongbudaan(4, 10)">
                        </div>

                        <div>
                            <input id="0" class="btn btn-default disabled" type="submit" value="开题11"
                                   onclick="kaiti(4, 11)">
                            <input id="0" class="btn btn-default disabled" type="submit" value="公布答案11"
                                   onclick="gongbudaan(4, 11)">
                        </div>

                    </div>
                    <input id="0" class="btn btn-default disabled" type="submit" value="结束第4轮" onclick="end_round(4)">

                </div>
                <br><br><br><br>

                <input id="0" class="btn btn-default disabled" type="submit" value="闭幕" onclick="bimu()">
            </div>


'''
import time

num = 0


def aaa():
    print('sdfsd')
    return 'sdfsdf'


for i in data.split('\n'):
    # print(i)
    ret = re.sub('id="\d+"', 'id="{}"'.format(num), i)
    if 'id=' in i:
        num += 1
    print(ret)
