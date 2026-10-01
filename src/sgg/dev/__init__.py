import numpy as np

from sgg.color import Color

from ._set_obj import _SET_OBJ
from ._set_obj_graph import _SET_OBJ_GRAPH
from .common._darray import *
from .common._dnumber import *
from .photo import Img_byte, Img_path
from .urls import linkcheck

__all__ = [
    "_is_str",
    "_SET_OBJ",
    "_SET_OBJ_GRAPH",
    "bols",
    "change_array_like",
    "Img_byte",
    "Img_path",
    "int0",
    "int0s",
    "int1s",
    "ints",
    "intsmin",
    "is_array_like",
    "linkcheck",
    "list2int",
    "list2num",
    "list4float",
    "listchose",
    "num0",
    "num0s",
    "num1s",
    "nums",
    "parsecolor",
    "range_num",
    "tonparray",
]


def parsecolor(val, other=None):
    if val is None:
        return other
    return str(Color(val))


def bols(j, o=True):
    if isinstance(j, bool) or (isinstance(j, np.generic) and j.dtype.kind is "b"):
        return j
    return o
