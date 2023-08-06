#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   __init__.py-tpl.py
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/6 10:54   Gnix       1.0         None
"""

from .generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from .viewsets import ModelViewSet, ReadOnlyModelViewSet
