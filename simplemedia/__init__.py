# -*- coding: utf-8 -*-
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from __future__ import unicode_literals

import os
import simplemedia
from .simplemedia import *

__all__ = simplemedia.__all__


def where():
    return os.path.dirname(__file__)
