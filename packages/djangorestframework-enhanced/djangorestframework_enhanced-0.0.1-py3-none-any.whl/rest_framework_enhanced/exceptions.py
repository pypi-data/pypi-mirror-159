#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   exceptions.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/5 23:24   Gnix       1.0         None
"""

from rest_framework.views import exception_handler
from django.http import Http404
from rest_framework.exceptions import APIException, NotAuthenticated
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, BadRequest
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from traceback import extract_tb
from rest_framework_enhanced.response import ResponseEx


def custom_exception_handler(exception, context):
    data = {}
    if isinstance(exception, FileNotFoundError):
        code = status.HTTP_404_NOT_FOUND
        msg = str(exception)
    elif isinstance(exception, ObjectDoesNotExist) or isinstance(exception, Http404):
        code = status.HTTP_404_NOT_FOUND
        msg = '对象不存在'
    elif isinstance(exception, PermissionDenied):
        code = status.HTTP_403_FORBIDDEN
        msg = '无访问权限'
    elif isinstance(exception, NotAuthenticated):
        code = status.HTTP_401_UNAUTHORIZED
        msg = exception.detail
    elif isinstance(exception, IntegrityError) or isinstance(exception, BadRequest):
        code = status.HTTP_400_BAD_REQUEST
        msg = str(exception)
    else:
        orig_response = exception_handler(exception, context)
        if orig_response and isinstance(exception, APIException):
            code = orig_response.status_code
            msg = "Framework Error:{}({})".format(exception, type(exception))

            try:
                for k, v in exception.detail.items():
                    data[k] = v
            except AttributeError:
                pass
        else:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR
            msg = '未知错误2'
    return ResponseEx(data=data, status=code, message=msg)


def make_exception_response(request, status_code, msg, data=None):
    response = ResponseEx(data=data, status=status_code, message=msg)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = 'application/json'
    response.renderer_context = {
        'view': request,
        'args': getattr(request, 'args', ()),
        'kwargs': getattr(request, 'kwargs', {}),
        'request': getattr(request, 'request', None)
    }
    return response


@csrf_exempt
def handler_404(request, exception):
    data = {
        'path': exception.args[0]["path"]
    }
    return make_exception_response(request, status.HTTP_404_NOT_FOUND, '页面不存在', data)


@csrf_exempt
def handler_500(request, *args):
    data = {}
    if settings.DEBUG:
        # exp_type = args[0]
        exp_obj = args[1]
        data['message'] = str(exp_obj)

        exp_trace = args[2]
        tb = extract_tb(exp_trace)
        line_list = []
        for item in tb:
            line_list.append({
                'file': item.filename,
                'function': item.name,
                'line': item.lineno,
            })
        if len(line_list) > 5:
            line_list = line_list[-5:]
        data['detail'] = line_list[::-1]

    return make_exception_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, '服务器内部错误', data)
