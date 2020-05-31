#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
import os
import shutil

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

this_dir = os.path.dirname(os.path.abspath(__file__))
addon_dir = os.path.join(this_dir, 'script.module.simplemedia')


def get_version():
    from io import open
    import re

    with open(os.path.join(addon_dir, 'addon.xml'), 'r', encoding='utf-8') as addon_xml:
        return re.search(r'(?<!xml )version="(.+?)"', addon_xml.read()).group(1)

language_dir = os.path.join('resources', 'language', 'English')
os.makedirs(os.path.join(this_dir, 'simplemedia', language_dir))

shutil.copy(os.path.join(addon_dir, 'libs', 'simplemedia.py'),
             os.path.join(this_dir, 'simplemedia'))
shutil.copy(os.path.join(addon_dir, 'addon.xml'),
             os.path.join(this_dir, 'simplemedia'))
shutil.copy(os.path.join(addon_dir, language_dir, 'strings.po'),
                 os.path.join(this_dir, 'simplemedia', language_dir))

try:
    setup(name='SimpleMedia',
          version=get_version(),
          description='SimpleMedia library for Kodi addons',
          author='vl.maksime',
          author_email='vl.maksime@gmail.com',
          url='https://github.com/vlmaksime/script.module.simplemedia',
          license='GPL v.3',
          packages=['simplemedia'],
          package_dir={'simplemedia': 'simplemedia'},
          package_data={'simplemedia': [os.path.join(language_dir, '*.po'), '*.xml']},
          zip_safe=False,
         )
finally:
    os.remove(os.path.join(this_dir, 'simplemedia', 'simplemedia.py'))
    os.remove(os.path.join(this_dir, 'simplemedia', 'addon.xml'))
    shutil.rmtree(os.path.join(this_dir, 'simplemedia', 'resources'))
