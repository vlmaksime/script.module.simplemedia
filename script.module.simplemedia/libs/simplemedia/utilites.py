# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals

import re

import xbmc

__all__ = ['Helper']


class Helper(object):

    @staticmethod
    def remove_html(text):
        if not text:
            return text

        result = text
        result = result.replace('&quot;', '\u0022')
        result = result.replace('&amp;', '\u0026')
        result = result.replace('&#39;', '\u0027')
        result = result.replace('&lt;', '\u003C')
        result = result.replace('&gt;', '\u003E')
        result = result.replace('&nbsp;', '\u00A0')
        result = result.replace('&laquo;', '\u00AB')
        result = result.replace('&raquo;', '\u00BB')
        result = result.replace('&ndash;', '\u2013')
        result = result.replace('&mdash;', '\u2014')
        result = result.replace('&lsquo;', '\u2018')
        result = result.replace('&rsquo;', '\u2019')
        result = result.replace('&sbquo;', '\u201A')
        result = result.replace('&ldquo;', '\u201C')
        result = result.replace('&rdquo;', '\u201D')
        result = result.replace('&bdquo;', '\u201E')
        result = result.replace('&hellip;', '\u22EF')

        return re.sub('<[^<]+?>', '', result)

    @classmethod
    def kodi_major_version(cls):
        return cls.kodi_version().split('.')[0]

    @staticmethod
    def kodi_version():
        return xbmc.getInfoLabel('System.BuildVersion').split(' ')[0]

    @staticmethod
    def get_keyboard_text(line='', heading='', hidden=False):
        kbd = xbmc.Keyboard(line, heading, hidden)
        kbd.doModal()
        if kbd.isConfirmed():
            return kbd.getText()

        return ''
