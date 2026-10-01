from sgg.widget.base import DOCElement, Element
# from sgg.widget.base.style import TTK_Style

__all__ = ["TElement", "DOCTElement"]

class TElement(Element, TTK_Style):
    def __init__(self, master, kw) -> None: ...
    def _padding_str(self, args): ...

class DOCTElement(DOCElement, TTK_Style):
    def __init__(self, master, kw) -> None: ...
