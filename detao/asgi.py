#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2018/2/10

import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "detao.settings")

channel_layer = get_channel_layer()
