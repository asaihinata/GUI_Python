from sgg.widgets.base.common import _WIDGET_OBJ,_WIDGETS_COMMON
from tkinter import Misc
from typing import Any
__all__ = ["Element"]
class Element(_WIDGETS_COMMON,_WIDGET_OBJ):
    _dict:dict[str,Any]
    def __init__(self, root:Misc|None=None, kw:dict={})->None:...