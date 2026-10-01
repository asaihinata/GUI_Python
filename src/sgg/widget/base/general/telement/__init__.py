from tkinter.ttk import Style

from sgg.widgets.base.general.element import Element

__all__ = ["TElement"]


class TElement(Element):
    def __init__(self, master=None, kw={}):
        super().__init__(master, kw)
        self._style = Style()
        self._dict["Styke"]=self._style
