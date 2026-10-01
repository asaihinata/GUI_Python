from re import findall
from types import FunctionType

import numpy as np
from matplotlib.colors import to_hex

from sgg.widgets.base.common import _WIDGET_OBJ,_WIDGETS_COMMON
from sgg._list import CURSOR_LIST
from sgg.font import TKFont

__all__ = ["Element", "DOCElement"]


class Element(_WIDGETS_COMMON,_WIDGET_OBJ):
    _dict={}
    def __init__(self, root=None, kw={}):
        self._dict = kw
        self._root = root
        self._back_bg = kw.get("back_bg")
        self._dict["root"]=self._root