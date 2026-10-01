from typing import overload

__all__ = ["Color"]

class Color:
    __slots__ = ("r", "g", "b", "a")
    @overload
    def __init__(self, r: str) -> None: ...
    @overload
    def __init__(self, r: int, g: int, b: int, a: int | float = 1.0) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str:
        """16進数カラーコードの値を返す"""

    def to_rgb(self) -> tuple[int, int, int]:
        """RGBの色の値をtupleで返す"""

    def to_rgba(self) -> tuple[int, int, int, float]:
        """RGBAの色の値をtupleで返す"""

    def to_rgb_str(self) -> str:
        """RGBの色の値を文字列で返す"""

    def to_rgba_str(self) -> str:
        """RGBAの色の値を文字列で返す"""

    def to_hex(
        self,
        with_alpha: bool | None = None,
        upper: bool = False,
    ) -> str:
        """16進数カラーコードの値を返す"""
