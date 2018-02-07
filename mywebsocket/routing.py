#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/1/30

from channels.routing import route
# channel_routing = [
#     route("http.request", "mywebsocket.consumers.http_consumer"),
# ]


from channels.routing import route
from .consumers import ws_connect, ws_disconnect, ws_receive

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route('websocket.receive', ws_receive)
]
