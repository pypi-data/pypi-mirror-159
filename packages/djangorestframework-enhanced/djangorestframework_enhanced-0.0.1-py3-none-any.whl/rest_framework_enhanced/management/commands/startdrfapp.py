#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@File    :   startdrfapp.py
@Contact :   madkarl@outlook.com
@License :   (C)Copyright 2022-2023, Gnix

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/7/15 23:16   Gnix       1.0         None
"""

import django
from django.core.management import BaseCommand, CommandError
from django.conf import settings
from importlib import import_module
from datetime import datetime

import os
import shutil

import stat
from pathlib import Path


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.verbosity = None
        self.rewrite_template_suffixes = (
            # Allow shipping invalid .py files without byte-compilation.
            (".py-tpl", ".py"),
        )

    def add_arguments(self, parser):
        parser.add_argument("name", help="Name of the drf application.")

    def handle(self, *args, **options):
        name = options.get('name')
        self.verbosity = options.get("verbosity")
        print(f'create new django-rest-framework application: {name}')

        self.validate_name(name)

        top_dir = os.path.join(os.getcwd(), name)
        try:
            os.makedirs(top_dir)
        except FileExistsError:
            raise CommandError("'%s' already exists" % top_dir)
        except OSError as e:
            raise CommandError(e)

        context = {
            'AUTHOR': settings.API_ENHANCED.get('AUTHOR') or 'None',
            'EMAIL': settings.API_ENHANCED.get('EMAIL') or 'None',
            'DATETIME': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'APPNAME': name,
            'APPNAME_CAMEL': "".join(x for x in name.title() if x != "_")
        }

        template_dir = str(
            Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.joinpath('template', 'drf_app'))
        prefix_length = len(template_dir) + 1

        excluded_directories = [".git", "__pycache__"]
        excluded_file_extensions = (".pyo", ".pyc", ".py.class")
        extensions = ('.py',)

        for root, dirs, files in os.walk(template_dir):
            relative_dir = root[prefix_length:]
            if relative_dir:
                target_dir = os.path.join(top_dir, relative_dir)
                os.makedirs(target_dir, exist_ok=True)

            for dirname in dirs[:]:
                if "exclude" not in options:
                    if dirname.startswith(".") or dirname == "__pycache__":
                        dirs.remove(dirname)
                elif dirname in excluded_directories:
                    dirs.remove(dirname)

            for filename in files:
                if filename.endswith(excluded_file_extensions):
                    continue
                old_path = os.path.join(root, filename)
                new_path = os.path.join(top_dir, relative_dir, filename)
                for old_suffix, new_suffix in self.rewrite_template_suffixes:
                    if new_path.endswith(old_suffix):
                        new_path = new_path[: -len(old_suffix)] + new_suffix
                        break  # Only rewrite once

                if os.path.exists(new_path):
                    raise CommandError(
                        "%s already exists. Overlaying an drf application into an existing "
                        "directory won't replace conflicting files." % (new_path,)
                    )

                # Only render the Python files, as we don't want to
                # accidentally render Django templates files
                file_name = os.path.basename(new_path)
                if new_path.endswith(extensions):
                    with open(old_path, encoding="utf-8") as template_file:
                        content = template_file.read()
                    content = content.replace('{$FILE}', file_name)
                    for k, v in context.items():
                        key = '{$' + k + '}'
                        content = content.replace(key, v)
                    with open(new_path, "w", encoding="utf-8") as new_file:
                        new_file.write(content)
                else:
                    shutil.copyfile(old_path, new_path)

                if self.verbosity >= 2:
                    self.stdout.write("Creating %s" % new_path)
                try:
                    shutil.copymode(old_path, new_path)
                    self.make_writeable(new_path)
                except OSError:
                    self.stderr.write(
                        "Notice: Couldn't set permission bits on %s. You're "
                        "probably using an uncommon filesystem setup. No "
                        "problem." % new_path,
                        self.style.NOTICE,
                    )

    def validate_name(self, name, name_or_dir="name"):
        if name is None:
            raise CommandError(
                "you must provide {an} {app} name".format(
                    an=self.a_or_an,
                    app=self.app_or_project,
                )
            )
        # Check it's a valid directory name.
        if not name.isidentifier():
            raise CommandError(
                "'{name}' is not a valid drf application. Please make sure the "
                "{type} is a valid identifier.".format(
                    name=name,
                    type=name_or_dir,
                )
            )
        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            raise CommandError(
                "'{name}' conflicts with the name of an existing Python "
                "module and cannot be used as an drf application. Please try "
                "another {type}.".format(
                    name=name,
                    type=name_or_dir,
                )
            )

    def make_writeable(self, filename):
        """
        Make sure that the file is writeable.
        Useful if our source is read-only.
        """
        if not os.access(filename, os.W_OK):
            st = os.stat(filename)
            new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
            os.chmod(filename, new_permissions)
