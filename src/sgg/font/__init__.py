"""フォントを設定するモジュール"""

from tkinter.font import Font, families, names, nametofont

__all__ = ["TKFont"]


class TKFont(Font):
    """フォントを設定するオブジェクト"""

    def __init__(self, root=None, font=None, name=None, **options):
        self.font_dict = {
            "family": "メイリオ",
            "size": 12,
            "weight": "normal",
            "slant": "roman",
            "underline": False,
            "overstrike": False,
        }
        if isinstance(font, Font):
            super().__init__(root=root, font=font, name=name)
        elif isinstance(font, tuple):
            default = ("メイリオ", 12, "normal", "roman", False, False)
            font = font + default[len(font) :]
            for i, key in enumerate(self.font_dict):
                self.font_dict[key] = font[i]
            super().__init__(root=root, name=name, **self.font_dict)
        else:
            for i in options:
                if i in self.font_dict and options[i] is not None:
                    self.font_dict[i] = options[i]
            super().__init__(root=root, name=name, **self.font_dict)
        family = self["family"]
        if family != "" and family not in TKFont.allfontname(root):
            raise NameError(f"{family}のフォント名は存在しません")

    @staticmethod
    def allfontname(root=None):
        return names(root) + families(root)

    @staticmethod
    def names(root=None):
        return names(root)

    @staticmethod
    def nametofont(name, root=None):
        return nametofont(name, root)

    @staticmethod
    def families(root=None, displayof=None):
        return families(root, displayof=displayof)
