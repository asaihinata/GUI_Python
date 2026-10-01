from re import findall
from tkinter import Tk,Misc
__all__=["_WIDGETS_COMMON"]
class _WIDGETS_COMMON:
    def winsize(self):
        root = self.root
        return root.winfo_width(), root.winfo_height()

    def winwidth(self):
        return self.root.winfo_width()

    def winheight(self):
        return self.root.winfo_height()

    def winxy(self):
        root = self.root
        return root.winfo_x(), root.winfo_y()

    def winx(self):
        return self.root.winfo_x()

    def winy(self):
        return self.root.winfo_y()

    def parent(self):
        return self.root.winfo_parent()

    def geometry(self):
        return [float(i) for i in findall(r"\d+", self.root.winfo_geometry())]

    def rootxy(self):
        root = self.root
        return root.winfo_rootx(), root.winfo_rooty()

    def rootx(self):
        return self.root.winfo_rootx()

    def rooty(self):
        return self.root.winfo_rooty()

    def visual(self):
        return self.root.winfo_visual()

    def screen(self):
        return self.root.winfo_screen()

    def reqsize(self):
        root = self.root
        return root.winfo_reqwidth(), root.winfo_reqheight()

    def reqwidth(self):
        return self.root.winfo_reqwidth()

    def reqheight(self):
        return self.root.winfo_reqheight()

    def id(self):
        return self.root.winfo_id()

    def name(self):
        return self.root.winfo_name()

    @property
    def root(self)->Tk|Misc:
        return self._root