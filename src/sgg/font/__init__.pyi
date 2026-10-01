"""フォントを設定するモジュール"""

from tkinter import Misc
from tkinter.font import Font
from typing import Literal, overload

__all__ = ["TKFont"]

type _FontDescription = (
    Font
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"], bool, bool]
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"], bool]
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"]]
    | tuple[str, int, Literal["normal", "bold"]]
    | tuple[str, int]
    | tuple[str]
)

class TKFont(Font):
    """フォントを設定するオブジェクト"""

    @overload
    def __init__(
        self,
        root: Misc | None = ...,
        font: _FontDescription = ...,
        name: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        root: Misc | None = ...,
        family: str = ...,
        size: int = ...,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        name: str | None = None,
    ) -> None: ...
    @staticmethod
    def allfontname(root: Misc | None = None) -> tuple[str, ...]: ...
    @staticmethod
    def names(root: Misc | None = None) -> tuple[str, ...]: ...
    @staticmethod
    def families(
        root: Misc | None = None, displayof: Misc | None = None
    ) -> tuple[str, ...]: ...
    @staticmethod
    def nametofont(name: str, root: Misc | None) -> Font: ...
