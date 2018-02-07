#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/1/30

import logging

from channels import Group
from channels.handler import AsgiHandler
from django.http import HttpResponse

# import const


logger = logging.getLogger(__name__)


def http_consumer(message):
    print('http:---->')
    response = HttpResponse(pp.pformat(message.content), content_type='text/plain')
    for chunk in AsgiHandler.encode_response(response):
        logger.debug(chunk)
        message.reply_channel.send(chunk)


def ws_connect(message):
    print('ws_conn: ------>', message.reply_channel)
    message.reply_channel.send({'accept': True})
    Group('testGroup').add(message.reply_channel)


def ws_disconnect(message):
    print('ws_disconn: ---->', message.content)
    Group('testGroup').discard(message.reply_channel)


def ws_receive(message):
    print('ws_recv: ---->', message.content)
    Group('testGroup').send({'text': '{}'.format(message.content.get('text'))})


def send_msg(msg):
    Group('testGroup').send({'text': 'send msg : {}'.format(msg)})
