# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals

import os
from .listitems import GeneralInfo, VideoInfo, ListItemInfo
from .webclient import WebClient, WebClientError

import simpleplugin
from simpleplugin import SimplePluginError, py2_decode, py2_encode

from .providers import Addon, MediaProvider, SearchProvider

__all__ = ['SimplePluginError', 'Plugin', 'RoutedPlugin', 'py2_encode', 'py2_decode', 'Addon',
           'GeneralInfo', 'VideoInfo', 'ListItemInfo',
           'WebClient', 'WebClientError']


class Plugin(simpleplugin.Plugin, MediaProvider, SearchProvider):

    def __init__(self, id_=''):
        super(Plugin, self).__init__(id_)


class RoutedPlugin(simpleplugin.RoutedPlugin, MediaProvider, SearchProvider):

    def __init__(self, id_=''):
        super(RoutedPlugin, self).__init__(id_)


def where():
    return os.path.dirname(__file__)
