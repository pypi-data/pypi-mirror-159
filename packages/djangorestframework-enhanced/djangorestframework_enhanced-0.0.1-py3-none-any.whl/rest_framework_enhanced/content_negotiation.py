#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   content_negotiation.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/4 23:46   Gnix       1.0         None
"""

from rest_framework.negotiation import DefaultContentNegotiation


class CustomContentNegotiation(DefaultContentNegotiation):
    """
    自定义内容协商器
    使浏览器请求API时，也返回JSON格式报文
    """

    def select_renderer(self, request, renderers, format_suffix=None):
        for render in renderers:
            if render.media_type == 'application/json':
                return render, render.media_type
        return super(CustomContentNegotiation, self).select_renderer(request, renderers, format_suffix)
