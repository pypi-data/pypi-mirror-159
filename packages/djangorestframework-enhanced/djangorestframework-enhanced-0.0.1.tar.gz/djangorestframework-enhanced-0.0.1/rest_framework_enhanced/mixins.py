#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   mixins.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/6 11:28   Gnix       1.0         None
"""

from rest_framework import mixins
from rest_framework_enhanced.response import ResponseEx


class CreateModelMixin(mixins.CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        response = super(CreateModelMixin, self).create(request, *args, **kwargs)
        return ResponseEx(data=response.data, status=response.status_code, headers=response.headers)


class ListModelMixin(mixins.ListModelMixin):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        response = super(ListModelMixin, self).list(request, *args, **kwargs)
        return ResponseEx(data=response.data, status=response.status_code)


class RetrieveModelMixin(mixins.RetrieveModelMixin):
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        response = super(RetrieveModelMixin, self).retrieve(request, *args, **kwargs)
        return ResponseEx(data=response.data, status=response.status_code)


class UpdateModelMixin(mixins.UpdateModelMixin):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        response = super(UpdateModelMixin, self).update(request, *args, **kwargs)
        return ResponseEx(data=response.data, status=response.status_code)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        response = super(UpdateModelMixin, self).partial_update(request, *args, **kwargs)
        return ResponseEx(data=response.data, status=response.status_code)


class DestroyModelMixin(mixins.DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        response = super(DestroyModelMixin, self).destroy(request, *args, **kwargs)
        return ResponseEx(status=response.status_code)
