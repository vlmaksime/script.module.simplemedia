#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

from setuptools import setup

this_dir = os.path.dirname(os.path.abspath(__file__))
addon_dir = os.path.join(this_dir, 'script.module.simplemedia')


def get_version():
    from io import open
    import re

    with open(os.path.join(addon_dir, 'addon.xml'), 'r', encoding='utf-8') as addon_xml:
        return re.search(r'(?<!xml )version="(.+?)"', addon_xml.read()).group(1)


shutil.copytree(os.path.join(addon_dir, 'libs', 'simplemedia'),
                os.path.join(this_dir, 'simplemedia'))

language_dir = os.path.join('resources', 'language', 'English')
os.makedirs(os.path.join(this_dir, 'simplemedia', language_dir))

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
          license='GPL-3.0-only',
          packages=['simplemedia'],
          package_dir={'simplemedia': 'simplemedia'},
          package_data={'simplemedia': [os.path.join(language_dir, '*.po'), '*.xml']},
          zip_safe=False,
          )
finally:
    shutil.rmtree(os.path.join(this_dir, 'simplemedia'))
