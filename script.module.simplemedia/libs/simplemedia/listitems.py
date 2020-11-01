# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals

__all__ = ['GeneralInfo', 'VideoInfo', 'ListItemInfo']


class GeneralInfo(object):

    @property
    def count(self):
        """
        integer (12) - can be used to store an id for later, or for sorting purposes

        :rtype: integer
        """

        pass

    @property
    def size(self):
        """
        long (1024) - size in bytes

        :rtype: long
        """

        pass

    @property
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
