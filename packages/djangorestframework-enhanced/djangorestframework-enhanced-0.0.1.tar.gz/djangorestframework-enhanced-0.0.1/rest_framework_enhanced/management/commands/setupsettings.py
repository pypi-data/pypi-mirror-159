#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   setupsettings.py    
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/7/18 15:00   Gnix       1.0         None
"""

from django.core.management import BaseCommand

import os

from pathlib import Path


class Command(BaseCommand):
    def handle(self, *args, **options):
        template_file = str(
            Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.joinpath('template', 'default_settings.txt'))

        with open(template_file, 'r', encoding='utf-8') as data:
            print('Setting Template:')
            print(data.read())

    def add_arguments(self, parser):
        parser.add_argument(
            '--author',
            '-a',
            dest='author',
            default='unknown'
        )
        parser.add_argument(
            '--email',
            '-e',
            dest='email',
            default='unknown'
        )
