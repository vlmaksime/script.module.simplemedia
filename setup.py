#!/usr/bin/env python
# coding: utf-8
# Author: Vladimir Maksimenko aka vl.maksime
# E-mail: vl.maksime@gmail.com

from __future__ import unicode_literals
import re
import os
import shutil
from io import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

this_dir = os.path.dirname(os.path.abspath(__file__))
addon_dir = os.path.join(this_dir, 'script.module.simplemedia')


def get_version():
    with open(os.path.join(addon_dir, 'addon.xml'), 'r', encoding='utf-8') as addon_xml:
        return re.search(r'(?<!xml )version="(.+?)"', addon_xml.read()).group(1)


shutil.copy(os.path.join(addon_dir, 'libs', 'simplemedia.py'), this_dir)
try:
    setup(name='SimpleMedia',
          version=get_version(),
          description='SimpleMedia library for Kodi addons',
          author='vl.maksime',
          author_email='vl.maksime@gmail.com',
          url='https://github.com/vlmaksime/script.module.simplemedia',
          license='GPL v.3',
          py_modules=['simplemedia'],
          zip_safe=False,
         )
finally:
    os.remove(os.path.join(this_dir, 'simplemedia.py'))
