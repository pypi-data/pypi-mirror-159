#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   pagination.py
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/9 18:11   Gnix       1.0         None
"""

from rest_framework import pagination


class StandardSizePagination(pagination.PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100


class LargeSizePagination(pagination.PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    page_size = 1000
    max_page_size = 10000
