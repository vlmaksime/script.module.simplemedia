# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals
from future.utils import iteritems
import re

import xbmc
import xbmcgui
import xbmcplugin

import simpleplugin

from simpleplugin import SimplePluginError, py2_decode, py2_encode

class MediaProvider(object):

    def __init__(self):
        self._handle = -1

    @staticmethod
    def create_list_item(item):
        major_version = xbmc.getInfoLabel('System.BuildVersion')[:2]
        if major_version >= '18':
            list_item = xbmcgui.ListItem(label=item.get('label', ''),
                                         label2=item.get('label2', ''),
                                         path=item.get('path', ''),
                                         offscreen=item.get('offscreen', False))
        else:
            list_item = xbmcgui.ListItem(label=item.get('label', ''),
                                         label2=item.get('label2', ''),
                                         path=item.get('path', ''))

        if major_version < '18':
            if item.get('info') \
              and item['info'].get('video'):
                for fields in ['genre', 'writer', 'director', 'country', 'credits']:
                    if item['info']['video'].get(fields) \
                      and isinstance(item['info']['video'][fields], list):
                        item['info']['video'][fields] = ' / '.join(item['info']['video'][fields])
        if major_version < '15':
            if item.get('info') \
              and item['info'].get('video'):
                if item['info']['video'].get('duration'):
                    item['info']['video']['duration'] = (item['info']['video']['duration'] / 60)

        if major_version >= '16':
            art = item.get('art', {})
            art['thumb'] = item.get('thumb', '')
            art['icon'] = item.get('icon', '')
            art['fanart'] = item.get('fanart', '')
            item['art'] = art
            cont_look = item.get('content_lookup')
            if cont_look is not None:
                list_item.setContentLookup(cont_look)
        else:
            list_item.setThumbnailImage(item.get('thumb', ''))
            list_item.setIconImage(item.get('icon', ''))
            list_item.setProperty('fanart_image', item.get('fanart', ''))
        if item.get('art'):
            list_item.setArt(item['art'])
        if item.get('stream_info'):
            for stream, stream_info in iteritems(item['stream_info']):
                list_item.addStreamInfo(stream, stream_info)
        if item.get('info'):
            for media, info in iteritems(item['info']):
                list_item.setInfo(media, info)
        if item.get('context_menu') is not None:
            list_item.addContextMenuItems(item['context_menu'])
        if item.get('subtitles'):
            list_item.setSubtitles(item['subtitles'])
        if item.get('mime'):
            list_item.setMimeType(item['mime'])
        if item.get('properties'):
            for key, value in iteritems(item['properties']):
                list_item.setProperty(key, value)
        if major_version >= '17':
            cast = item.get('cast')
            if cast is not None:
                list_item.setCast(cast)
            db_ids = item.get('online_db_ids')
            if db_ids is not None:
                list_item.setUniqueIDs(db_ids)
            ratings = item.get('ratings')
            if ratings is not None:
                for rating in ratings:
                    list_item.setRating(**rating)
        return list_item

    def create_directory(self, items, content='files', succeeded=True, update_listing=False, category=None, sort_methods=None, cache_to_disk=False, total_items=0):
        xbmcplugin.setContent(self._handle, content)

        if category is not None:
            xbmcplugin.setPluginCategory(self._handle, category)

        if sort_methods is not None:
            if isinstance(sort_methods, int):
                xbmcplugin.addSortMethod(self._handle, sort_methods)
            elif isinstance(sort_methods, (tuple, list)):
                for method in sort_methods:
                    xbmcplugin.addSortMethod(self._handle, method)
            else:
                raise TypeError(
                    'sort_methods parameter must be of int, tuple or list type!')

        for item in items:
            is_folder = item.get('is_folder', True)
            list_item = self.create_list_item(item)
            if item.get('is_playable'):
                list_item.setProperty('IsPlayable', 'true')
                is_folder = False
            xbmcplugin.addDirectoryItem(self._handle, item['url'], list_item, is_folder, total_items)
        xbmcplugin.endOfDirectory(self._handle, succeeded, update_listing, cache_to_disk)

    def resolve_url(self, item, succeeded=True):
        list_item = self.create_list_item(item)
        xbmcplugin.setResolvedUrl(self._handle, succeeded, list_item)

class Helper(object):

    @staticmethod
    def remove_html(text):
        if not text:
            return text

        result = text
        result = result.replace(u'&nbsp;',      u' ')
        result = result.replace(u'&pound;',     u'£')
        result = result.replace(u'&euro;',      u'€')
        result = result.replace(u'&para;',      u'¶')
        result = result.replace(u'&sect;',      u'§')
        result = result.replace(u'&copy;',      u'©')
        result = result.replace(u'&reg;',       u'®')
        result = result.replace(u'&trade;',     u'™')
        result = result.replace(u'&deg;',       u'°')
        result = result.replace(u'&plusmn;',    u'±')
        result = result.replace(u'&frac14;',    u'¼')
        result = result.replace(u'&frac12;',    u'½')
        result = result.replace(u'&frac34;',    u'¾')
        result = result.replace(u'&times;',     u'×')
        result = result.replace(u'&divide;',    u'÷')
        result = result.replace(u'&fnof;',      u'ƒ')
        result = result.replace(u'&Alpha;',     u'Α')
        result = result.replace(u'&Beta;',      u'Β')
        result = result.replace(u'&Gamma;',     u'Γ')
        result = result.replace(u'&Delta;',     u'Δ')
        result = result.replace(u'&Epsilon;',   u'Ε')
        result = result.replace(u'&Zeta;',      u'Ζ')
        result = result.replace(u'&Eta;',       u'Η')
        result = result.replace(u'&Theta;',     u'Θ')
        result = result.replace(u'&Iota;',      u'Ι')
        result = result.replace(u'&Kappa;',     u'Κ')
        result = result.replace(u'&Lambda;',    u'Λ')
        result = result.replace(u'&Mu;',        u'Μ')
        result = result.replace(u'&Nu;',        u'Ν')
        result = result.replace(u'&Xi;',        u'Ξ')
        result = result.replace(u'&Omicron;',   u'Ο')
        result = result.replace(u'&Pi;',        u'Π')
        result = result.replace(u'&Rho;',       u'Ρ')
        result = result.replace(u'&Sigma;',     u'Σ')
        result = result.replace(u'&Tau;',       u'Τ')
        result = result.replace(u'&Upsilon;',   u'Υ')
        result = result.replace(u'&Phi;',       u'Φ')
        result = result.replace(u'&Chi;',       u'Χ')
        result = result.replace(u'&Psi;',       u'Ψ')
        result = result.replace(u'&Omega;',     u'Ω')
        result = result.replace(u'&alpha;',     u'α')
        result = result.replace(u'&beta;',      u'β')
        result = result.replace(u'&gamma;',     u'γ')
        result = result.replace(u'&delta;',     u'δ')
        result = result.replace(u'&epsilon;',   u'ε')
        result = result.replace(u'&zeta;',      u'ζ')
        result = result.replace(u'&eta;',       u'η')
        result = result.replace(u'&theta;',     u'θ')
        result = result.replace(u'&iota;',      u'ι')
        result = result.replace(u'&kappa;',     u'κ')
        result = result.replace(u'&lambda;',    u'λ')
        result = result.replace(u'&mu;',        u'μ')
        result = result.replace(u'&nu;',        u'ν')
        result = result.replace(u'&xi;',        u'ξ')
        result = result.replace(u'&omicron;',   u'ο')
        result = result.replace(u'&pi;',        u'π')
        result = result.replace(u'&rho;',       u'ρ')
        result = result.replace(u'&sigmaf;',    u'ς')
        result = result.replace(u'&sigma;',     u'σ')
        result = result.replace(u'&tau;',       u'τ')
        result = result.replace(u'&upsilon;',   u'υ')
        result = result.replace(u'&phi;',       u'φ')
        result = result.replace(u'&chi;',       u'χ')
        result = result.replace(u'&psi;',       u'ψ')
        result = result.replace(u'&omega;',     u'ω')
        result = result.replace(u'&larr;',      u'←')
        result = result.replace(u'&uarr;',      u'↑')
        result = result.replace(u'&rarr;',      u'→')
        result = result.replace(u'&darr;',      u'↓')
        result = result.replace(u'&harr;',      u'↔')
        result = result.replace(u'&spades;',    u'♠')
        result = result.replace(u'&clubs;',     u'♣')
        result = result.replace(u'&hearts;',    u'♥')
        result = result.replace(u'&diams;',     u'♦')
        result = result.replace(u'&quot;',      u'"')
        result = result.replace(u'&amp;',       u'&')
        result = result.replace(u'&lt;',        u'<')
        result = result.replace(u'&gt;',        u'>')
        result = result.replace(u'&hellip;',    u'…')
        result = result.replace(u'&prime;',     u'′')
        result = result.replace(u'&Prime;',     u'″')
        result = result.replace(u'&ndash;',     u'–')
        result = result.replace(u'&mdash;',     u'—')
        result = result.replace(u'&lsquo;',     u'‘')
        result = result.replace(u'&rsquo;',     u'’')
        result = result.replace(u'&sbquo;',     u'‚')
        result = result.replace(u'&ldquo;',     u'“')
        result = result.replace(u'&rdquo;',     u'”')
        result = result.replace(u'&bdquo;',     u'„')
        result = result.replace(u'&laquo;',     u'«')
        result = result.replace(u'&raquo;',     u'»')

        # result = result.replace(u'<br>',    u'\n')

        return re.sub('<[^<]+?>', '', result)

    def get_image(self, image):
        return image if xbmc.skinHasImage(image) else self.icon

    def notify_error(self, err):
        self.log_error(err)
        try:
            message = self.gettext(err)
        except:
            message = py2_decode(err)
    
        xbmcgui.Dialog().notification(self.name, message, xbmcgui.NOTIFICATION_ERROR)

class Plugin(simpleplugin.Plugin, MediaProvider, Helper):
    pass

class RoutedPlugin(simpleplugin.RoutedPlugin, MediaProvider, Helper):
    pass