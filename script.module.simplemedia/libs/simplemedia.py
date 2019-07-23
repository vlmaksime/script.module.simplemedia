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

__all__ = ['SimplePluginError', 'Plugin', 'RoutedPlugin', 'py2_encode', 'py2_decode',
           'GeneralInfo', 'VideoInfo', 'ListItemInfo']

class GeneralInfo(object):
    
    @property
    def count(self):
        """
        integer (12) - can be used to store an id for later, or for sorting purposes

        :rtype: integer
        """
        
        pass
         
    def size(self):
        """
        long (1024) - size in bytes

        :rtype: long
        """
        
        pass
     
    def date(self):
        """
        string (d.m.Y / 01.01.2009) - file date

        :rtype: string
        """
        
        pass
                
    def get_info(self):
        return self._get_info(GeneralInfo)

    def _get_info(self, cls, result=None):
        result = result or {}
        
        for atr_name in dir(cls):
            atr_info = cls.__dict__.get(atr_name)
            if atr_info is not None \
              and isinstance(atr_info, property):
                atr_value = getattr(self, atr_name)
                if atr_value is not None:
                    result[atr_name] = atr_value
        
        return result
    
class VideoInfo(GeneralInfo):

    @property
    def genre(self):
        """
        string (Comedy) or list of strings (["Comedy", "Animation", "Drama"])

        :rtype: string or list of strings
        """
        
        pass

    @property
    def country(self):
        """
        string (Germany) or list of strings (["Germany", "Italy", "France"])

        :rtype: string or list of strings
        """
        
        pass

    @property
    def year(self):
        """
        integer (2009)

        :rtype: integer
        """
        
        pass

    @property
    def episode(self):
        """
        integer (4)

        :rtype: integer
        """
        
        pass

    @property
    def season(self):
        """
        integer (1)

        :rtype: integer
        """
        
        pass

    @property
    def sortepisode(self):
        """
        integer (4)

        :rtype: integer
        """
        
        return self.episode

    @property
    def sortseason(self):
        """
        integer (1)

        :rtype: integer
        """
        
        return self.season

    @property
    def episodeguide(self):
        """
        string (Episode guide)

        :rtype: string
        """
        
        pass

    @property
    def showlink(self):
        """
        string (Battlestar Galactica) or list of strings (["Battlestar Galactica", "Caprica"])

        :rtype: string or list of strings
        """
        
        pass

    @property
    def top250(self):
        """
        integer (192)

        :rtype: integer
        """
        
        pass

    @property
    def setid(self):
        """
        integer (14)

        :rtype: integer
        """
        
        pass

    @property
    def tracknumber(self):
        """
        integer (3)

        :rtype: integer
        """
        
        pass

    @property
    def rating(self):
        """
        float (6.4) - range is 0..10

        :rtype: float
        """
        
        pass

    @property
    def userrating(self):
        """
        integer (9) - range is 1..10 (0 to reset)

        :rtype: integer
        """
        
        pass

    @property
    def playcount(self):
        """
        integer (2) - number of times this item has been played

        :rtype: integer
        """
        
        pass

    @property
    def overlay(self):
        """
        integer (2) - range is 0..7. See Overlay icon types for values

        :rtype: integer
        """
        
        pass

    @property
    def cast(self):
        """
        list (["Michal C. Hall","Jennifer Carpenter"]) - if provided a list of tuples cast will be interpreted as castandrole

        :rtype: list
        """
        
        pass

    @property
    def castandrole(self):
        """
        list of tuples ([("Michael C. Hall","Dexter"),("Jennifer Carpenter","Debra")])

        :rtype: list
        """
        
        pass
        
    @property
    def director(self):
        """
        string (Dagur Kari) or list of strings (["Dagur Kari", "Quentin Tarantino", "Chrstopher Nolan"])

        :rtype: string or list of strings
        """
        
        pass
    
    @property
    def mpaa(self):
        """
        string (PG-13)
        
        :rtype: string
        """
        
        pass
    
    @property
    def plot(self):
        """
        string (Long Description)
        
        :rtype: string
        """
        
        pass
    
    @property
    def plotoutline(self):
        """
        string (Short Description)
        
        :rtype: string
        """
        
        pass

    @property
    def title(self):
        """
        string (Big Fan)
        
        :rtype: string
        """
        
        pass

    @property
    def originaltitle(self):
        """
        string (Big Fan)
        
        :rtype: string
        """
        
        pass

    @property
    def sorttitle(self):
        """
        string (Big Fan)
        
        :rtype: string
        """
        
        return self.title

    @property
    def duration(self):
        """
        integer (245) - duration in seconds

        :rtype: integer
        """
        
        pass

    @property
    def studio(self):
        """
        string (Warner Bros.) or list of strings (["Warner Bros.", "Disney", "Paramount"])

        :rtype: string or list of strings
        """
        
        pass

    @property
    def tagline(self):
        """
        string (An awesome movie) - short description of movie

        :rtype: string
        """
        
        pass

    @property
    def writer(self):
        """
        string (Robert D. Siegel) or list of strings (["Robert D. Siegel", "Jonathan Nolan", "J.K. Rowling"])

        :rtype: string or list of strings
        """
        
        pass

    @property
    def tvshowtitle(self):
        """
        string (Heroes)

        :rtype: string
        """
        
        pass

    @property
    def premiered(self):
        """
        string (2005-03-04)

        :rtype: string
        """
        
        pass

    @property
    def status(self):
        """
        string (Continuing) - status of a TVshow

        :rtype: string
        """
        
        pass

    @property
    def set(self):
        """
        string (Batman Collection) - name of the collection

        :rtype: string
        """
        
        pass

    @property
    def setoverview(self):
        """
        string (All Batman movies) - overview of the collection

        :rtype: string
        """
        
        pass

    @property
    def tag(self):
        """
        string (cult) or list of strings (["cult", "documentary", "best movies"]) - movie tag

        :rtype: string or list of strings
        """
        
        pass

    @property
    def imdbnumber(self):
        """
        string (tt0110293) - IMDb code

        :rtype: string
        """
        
        pass
    
    @property
    def code(self):
        """
        string (101) - Production code

        :rtype: string
        """
        
        pass
    
    @property
    def aired(self):
        """
        string (2008-12-07)

        :rtype: string
        """
        
        pass
    
    @property
    def credits(self):
        """
        string (Andy Kaufman) or list of strings (["Dagur Kari", "Quentin Tarantino", "Chrstopher Nolan"]) - writing credits

        :rtype: string or list of strings
        """
        
        pass

    @property
    def lastplayed(self):
        """
        string (Y-m-d h:m:s = 2009-04-05 23:16:04)

        :rtype: string
        """
        
        pass

    @property
    def album(self):
        """
        string (The Joshua Tree)

        :rtype: string
        """
        
        pass

    @property
    def artist(self):
        """
        list (['U2'])

        :rtype: list
        """
        
        pass

    @property
    def votes(self):
        """
        string (12345 votes)

        :rtype: string
        """
        
        pass

    @property
    def path(self):
        """
        string (/home/user/movie.avi)

        :rtype: string
        """
        
        pass

    @property
    def trailer(self):
        """
        string (/home/user/trailer.avi)

        :rtype: string
        """
        
        pass

    @property
    def dateadded(self):
        """
        string (Y-m-d h:m:s = 2009-04-05 23:16:04)

        :rtype: string
        """
        
        pass
     
    @property
    def mediatype(self):
        """
        string - "video", "movie", "tvshow", "season", "episode" or "musicvideo"

        :rtype: string
        """
        
        pass
     
    @property
    def dbid(self):
        """
        integer (23) - Only add this for items which are part of the local db. You also need to set the correct 'mediatype'!

        :rtype: integer
        """
        
        pass    

    def get_info(self):
        video_info = self._get_info(VideoInfo)
        return self._get_info(GeneralInfo, video_info)

class ListItemInfo(object):

    @property
    def label(self):
        pass

    @property
    def label2(self):
        pass

    @property
    def path(self):
        pass

    @property
    def offscreen(self):
        pass

    @property
    def is_folder(self):
        pass

    @property
    def is_playable(self):
        pass

    @property
    def art(self):
        pass

    @property
    def thumb(self):
        pass

    @property
    def icon(self):
        pass

    @property
    def fanart(self):
        pass

    @property
    def content_lookup(self):
        return False

    @property
    def stream_info(self):
        pass

    @property
    def info(self):
        pass
    
    @property
    def context_menu(self):
        pass
       
    @property
    def subtitles(self):
        pass

    @property
    def mime(self):
        pass

    @property
    def properties(self):
        pass

    @property
    def cast(self):
        pass

    @property
    def online_db_ids(self):
        pass

    @property
    def ratings(self):
        pass

    @property
    def url(self):
        pass
    
    @property
    def season(self):
        pass
    
    def get_item(self):
        result = {}
        
        cls = ListItemInfo
        for atr_name in dir(cls):
            atr_info = cls.__dict__.get(atr_name)
            if atr_info is not None \
              and isinstance(atr_info, property):
                atr_value = getattr(self, atr_name)
                if atr_value is not None:
                    result[atr_name] = atr_value
        
        return result

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
            if item.get('info') is not None\
              and item['info'].get('video') is not None:
                for field in ['genre', 'writer', 'director', 'country', 'credits']:
                    field_value = item['info']['video'].get(field)
                    if field_value is not None \
                      and isinstance(field_value, list):
                        item['info']['video'][field] = ' / '.join(field_value)

        if major_version < '17':
            if item.get('info') is not None \
              and item['info'].get('video') is not None:
                rating = item['info']['video'].get('rating')
                ratings = item.get('ratings')
                if ratings is not None \
                  and rating is None:
                    for rating_item in ratings:
                        if rating_item['defaultt']:
                            item['info']['video']['rating'] = rating_item['rating']
                            if rating_item['votes']:
                                item['info']['video']['votes'] = rating_item['votes']
                            break

        if major_version < '15':
            if item.get('info') is not None\
              and item['info'].get('video') is not None:
                duration = item['info']['video'].get('duration')
                if duration is not None:
                    item['info']['video']['duration'] = duration / 60

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

        if major_version >= '18':
            season = item.get('season')
            if season is not None:
                list_item.addSeason(**season)

        return list_item

    def create_directory(self, items, content='files', succeeded=True, update_listing=False, category=None, sort_methods=None, cache_to_disk=False, total_items=0):
        xbmcplugin.setContent(self._handle, content)

        if category is not None:
            xbmcplugin.setPluginCategory(self._handle, category)

        if sort_methods is not None:
            if isinstance(sort_methods, (int, dict)):
                sort_methods = [sort_methods]
            elif isinstance(sort_methods, (tuple, list)):
                sort_methods = sort_methods
            else:
                raise TypeError(
                    'sort_methods parameter must be of int, dict, tuple or list type!')
            for method in sort_methods:
                if isinstance(method, int):
                    xbmcplugin.addSortMethod(self._handle, method)
                elif isinstance(method, dict):
                    xbmcplugin.addSortMethod(self._handle, **method)
                else:
                    raise TypeError(
                        'method parameter must be of int or dict type!')

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

class SearchProvider(object):

    def search_history_items(self):
    
        sm = simpleplugin.Addon('script.module.simplemedia')
        _ = sm.initialize_gettext()

        search_icon = self.get_image('DefaultAddonsSearch.png')

        listitem = {'label': _('New Search...'),
                        'url': self.url_for('search'),
                        'icon': search_icon,
                        'fanart': self.fanart,
                        'is_folder': False,
                        'is_playable': False,
                        'content_lookup': False,
                        }
        yield listitem

        with self.get_storage('__history__.pcl') as storage:
            history = storage.get('history', [])

            history_length = self.get_setting('history_length')
            if len(history) > history_length:
                history[history_length - len(history):] = []

            for item in history:
                if isinstance(item, dict):
                    keyword = py2_encode(item['keyword']) # backward compatibility
                else:
                    keyword = item
    
                listitem = {'label': keyword,
                            'url': self.url_for('search', keyword=keyword),
                            'icon': search_icon,
                            'fanart': self.fanart,
                            'content_lookup': False,
                            }
                yield listitem

    def update_search_history(self, keyword):

        with self.get_storage('__history__.pcl') as storage:
            history = storage.get('history', [])
            
            if keyword in history:
                history.remove(keyword)

            history.insert(0, keyword)

            history_length = self.get_setting('history_length')
            if len(history) > history_length:
                history[history_length - len(history):] = []

            storage['history'] = history


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
        result = result.replace(u'&#39;',       u'\'')

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

    def set_settings(self, settings):
        for id_, val in iteritems(settings):
            if self.get_setting(id_) != val:
                self.set_setting(id_, val)

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
    
class Plugin(simpleplugin.Plugin, MediaProvider, Helper, SearchProvider):
    pass

class RoutedPlugin(simpleplugin.RoutedPlugin, MediaProvider, Helper, SearchProvider):
    pass