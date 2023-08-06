#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   response.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/6 10:40   Gnix       1.0         None
"""

from rest_framework.response import Response


class ResponseEx(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None, **kwargs):
        super(ResponseEx, self).__init__(data, status, template_name, headers, exception, content_type)
        self.data = {
            'code': int(status),
        }
        if data:
            self.data['data'] = data
        self.data.update(kwargs)
