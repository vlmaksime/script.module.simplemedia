# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import unittest

import xbmcaddon

cwd = os.path.dirname(os.path.abspath(__file__))

addon_name = 'script.module.simplemedia'

temp_dir = os.path.join(cwd, 'addon_data')

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

addon_dir = os.path.join(cwd, addon_name)
addon_config_dir = os.path.join(temp_dir, addon_name)
xbmcaddon.init_addon(addon_dir, addon_config_dir, True)

# Import our module being tested
sys.path.append(os.path.join(addon_dir, 'libs'))

# Begin tests

if __name__ == '__main__':
    unittest.main()
