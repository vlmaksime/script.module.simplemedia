# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals

import json

import simpleplugin
import xbmc
import xbmcgui
import xbmcplugin
from future.utils import iteritems
from simpleplugin import py2_decode, py2_encode

from .dialogs import Dialogs
from .utilites import Helper

__all__ = ['Addon', 'MediaProvider', 'SearchProvider']


class Addon(simpleplugin.Addon, Helper, Dialogs):

    def __init__(self, id_=''):
        super(Addon, self).__init__(id_)

    def get_image(self, image):
        return image if xbmc.skinHasImage(image) else self.icon

    def set_settings(self, settings):
        for id_, val in iteritems(settings):
            if self.get_setting(id_) != val:
                self.set_setting(id_, val)

    def send_notification(self, message, data=None):
        params = {'sender': self.id,
                  'message': message,
                  }

        if data is not None:
            params['data'] = data

        command = json.dumps({'jsonrpc': '2.0',
                              'method': 'JSONRPC.NotifyAll',
                              'params': params,
                              'id': 1,
                              })

        result = xbmc.executeJSONRPC(command)

    @staticmethod
    def simplemedia_gettext():

        addon = simpleplugin.Addon('script.module.simplemedia')
        return addon.initialize_gettext()


class MediaProvider(Addon):

    def create_list_item(self, item):
        major_version = self.kodi_major_version()
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
            if item.get('info') is not None \
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
            if item.get('info') is not None \
                    and item['info'].get('video') is not None:
                duration = item['info']['video'].get('duration')
                if duration is not None:
                    item['info']['video']['duration'] = duration / 60

                mediatype = item['info']['video'].get('mediatype')
                if mediatype in ['episode', 'season']:
                    art = item.get('art', {})
                    if art.get('poster') is None:
                        if art.get('season.poster') is not None:
                            item['art']['poster'] = art['season.poster']
                        elif art.get('tvshow.poster') is not None:
                            item['art']['poster'] = art['tvshow.poster']

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
                if major_version >= '20':
                    self.set_info_tag(list_item, media, info)
                else:
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

    def create_directory(self, items, content='files', succeeded=True, update_listing=False, category=None,
                         sort_methods=None, cache_to_disk=False, total_items=0):
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

    def set_info_tag(self, list_item, media, info):

        if media == 'video':
            self.set_video_info_tag(list_item, info)
        else:
            raise TypeError(
                'unsupported media type "{0}"!'.format(media))

    @staticmethod
    def set_video_info_tag(list_item, info):

        videoInfoTag = list_item.getVideoInfoTag()
        for tag, value in iteritems(info):
            if value is None \
                    or tag in ['date']:
                continue
            elif tag == 'dbid':
                videoInfoTag.setDbId(value)
            elif tag == 'year':
                videoInfoTag.setYear(value)
            elif tag == 'episode':
                videoInfoTag.setEpisode(value)
            elif tag == 'season':
                videoInfoTag.setSeason(value)
            elif tag == 'sortepisode':
                videoInfoTag.setSortEpisode(value)
            elif tag == 'sortseason':
                videoInfoTag.setSortSeason(value)
            elif tag == 'episodeguide':
                videoInfoTag.setEpisodeGuide(value)
            elif tag == 'top250':
                videoInfoTag.setTop250(value)
            elif tag == 'setid':
                videoInfoTag.setSetId(value)
            elif tag == 'tracknumber':
                videoInfoTag.setTrackNumber(value)
            elif tag == 'rating':
                videoInfoTag.setRating(value)
            elif tag == 'ratings':
                ratings = []
                defaultrating = ''
                for item in value:
                    ratings[item['type']] = (item.get('rating', 0), item.get('votes', 0))
                    if item['defaultt']:
                        defaultrating = rating_item['type']
                videoInfoTag.setRatings(ratings, defaultrating)

            elif tag == 'userrating':
                videoInfoTag.setUserRating(value)
            elif tag == 'playcount':
                videoInfoTag.setPlaycount(value)
            elif tag == 'mpaa':
                videoInfoTag.setMpaa(value)
            elif tag == 'plot':
                videoInfoTag.setPlot(value)
            elif tag == 'plotoutline':
                videoInfoTag.setPlotOutline(value)
            elif tag == 'title':
                videoInfoTag.setTitle(value)
            elif tag == 'originaltitle':
                videoInfoTag.setOriginalTitle(value)
            elif tag == 'sorttitle':
                videoInfoTag.setSortTitle(value)
            elif tag == 'tagline':
                videoInfoTag.setTagLine(value)
            elif tag == 'tvshowtitle':
                videoInfoTag.setTvShowTitle(value)
            elif tag == 'status':
                videoInfoTag.setTvShowStatus(value)
            elif tag == 'genre':
                videoInfoTag.setGenres(value)
            elif tag == 'country':
                videoInfoTag.setCountries(value)
            elif tag == 'director':
                videoInfoTag.setDirectors(value)
            elif tag == 'studio':
                videoInfoTag.setStudios(value)
            elif tag == 'writer':
                videoInfoTag.setWriters(value)
            elif tag == 'duration':
                if isinstance(value, float):
                    value = int(value)
                videoInfoTag.setDuration(value)
            elif tag == 'premiered':
                videoInfoTag.setPremiered(value)
            elif tag == 'set':
                videoInfoTag.setSet(value)
            elif tag == 'setoverview':
                videoInfoTag.setSetOverview(value)
            elif tag == 'tag':
                videoInfoTag.setTags(value)
            elif tag == 'code':
                videoInfoTag.setProductionCode(value)
            elif tag == 'aired':
                videoInfoTag.setFirstAired(value)
            elif tag == 'lastplayed':
                videoInfoTag.setLastPlayed(value)
            elif tag == 'album':
                videoInfoTag.setAlbum(value)
            elif tag == 'votes':
                videoInfoTag.setVotes(value)
            elif tag == 'trailer':
                videoInfoTag.setTrailer(value)
            elif tag == 'path':
                videoInfoTag.setPath(value)
            elif tag == 'filenameandpath':
                videoInfoTag.setFilenameAndPath(value)
            elif tag == 'imdbnumber':
                videoInfoTag.setIMDBNumber(value)
            elif tag == 'dateadded':
                videoInfoTag.setDateAdded(value)
            elif tag == 'mediatype':
                videoInfoTag.setMediaType(value)
            elif tag == 'showlink':
                videoInfoTag.setShowLinks(value)
            elif tag == 'artist':
                videoInfoTag.setArtists(value)
            elif tag == 'cast':
                cast = []
                for actor in value:
                    actor_name = ''
                    actor_role = ''
                    actor_order = 0
                    actor_thumbnail = ''
                    if isinstance(actor, dict):
                        actor_name = actor.get('name', '')
                        actor_role = actor.get('role', '')
                        actor_order = actor.get('order', 0)
                        actor_thumbnail = actor.get('thumbnail', '')
                    else:
                        actor_name = actor
                    cast.append(xbmc.Actor(actor_name, actor_role, actor_order, actor_thumbnail))
                videoInfoTag.setCast(cast)
            else:
                raise TypeError(
                    'unsupported info tag "{0}" with value "{1}"!'.format(tag, value))


class SearchProvider(Addon):

    def search_history_items(self):

        search_icon = self.get_image('DefaultAddonsSearch.png')

        _ = self.simplemedia_gettext()

        listitem = {'label': _('New Search...'),
                    'url': self.url_for('search'),
                    'icon': search_icon,
                    'fanart': self.fanart,
                    'properties': {'SpecialSort': 'top'},
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

            _ = self.simplemedia_gettext()
            clear_item = (_('Clear \'Search\''), 'RunPlugin({0})'.format(self.url_for('search_clear')))

            for index, item in enumerate(history):
                if isinstance(item, dict):
                    keyword = py2_encode(item['keyword'])  # backward compatibility
                else:
                    keyword = item

                remove_item = (_('Remove from \'Search\''), 'RunPlugin({0})'.format(self.url_for('search_remove', index=index)))

                listitem = {'label': keyword,
                            'url': self.url_for('search', keyword=keyword),
                            'icon': search_icon,
                            'fanart': self.fanart,
                            'context_menu': [remove_item, clear_item],
                            'content_lookup': False,
                            }
                yield listitem

    def update_search_history(self, keyword):

        with self.get_storage('__history__.pcl') as storage:
            history = storage.get('history', [])

            keyword = py2_decode(keyword)

            i = 0
            keyword_lower = keyword.lower()
            while i < len(history):
                item = history[i]
                if isinstance(item, dict):
                    item_keyword = item['keyword']  # backward compatibility
                else:
                    item_keyword = item
                item_keyword = py2_decode(item_keyword).lower()

                if item_keyword == keyword_lower:
                    del history[i]
                else:
                    i += 1

            history.insert(0, keyword)

            history_length = self.get_setting('history_length')
            if len(history) > history_length:
                history[history_length - len(history):] = []

            storage['history'] = history

    def search_history_remove(self, index):

        with self.get_storage('__history__.pcl') as storage:
            history = storage.get('history', [])

            del history[index]

            storage['history'] = history

        _ = self.simplemedia_gettext()

        self.dialog_notification_info(_('Successfully removed from \'Search\''))
        xbmc.executebuiltin('Container.Refresh()')

    def search_history_clear(self):

        with self.get_storage('__history__.pcl') as storage:
            storage['history'] = []

        _ = self.simplemedia_gettext()

        self.dialog_notification_info(_('\'Search\' successfully cleared'))
        xbmc.executebuiltin('Container.Refresh()')
