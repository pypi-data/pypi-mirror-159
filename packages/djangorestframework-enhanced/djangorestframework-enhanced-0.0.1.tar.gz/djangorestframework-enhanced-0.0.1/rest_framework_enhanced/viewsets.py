#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   viewsets.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/6 11:20   Gnix       1.0         None
"""

from rest_framework import viewsets
from rest_framework_enhanced import mixins


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
