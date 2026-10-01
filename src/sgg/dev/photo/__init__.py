from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image

__all__ = ["Img_byte", "Img_path"]


class Img_conversion:
    def __init__(self, data):
        self.__imgs = Image.open(data)

    @property
    def image(self):
        return self.__imgs

    @property
    def width(self):
        return self.__imgs.width

    def get_width(self):
        return self.__imgs.width

    @property
    def height(self):
        return self.__imgs.height

    def get_height(self):
        return self.__imgs.height

    @property
    def size(self):
        return self.__imgs.width, self.__imgs.height

    def get_size(self):
        return self.__imgs.width, self.__imgs.height

    @property
    def format(self):
        return self.__imgs.format

    def get_format(self):
        return self.__imgs.format

    @property
    def mode(self):
        return self.__imgs.mode

    def get_mode(self):
        return self.__imgs.mode

    def show(self, title=None):
        self.__imgs.show(title)

    def resize(self, w, h):
        if not isinstance(w, int):
            raise TypeError("wには整数型を指定してください")
        elif w <= 1:
            raise ValueError("wには1以上の整数を指定してください")
        if not isinstance(h, int):
            raise TypeError("hには整数型を指定してください")
        elif h <= 1:
            raise ValueError("hには1以上の整数を指定してください")
        self.__imgs.resize((w, h))
        return self

    def asresize(self):
        self.__imgs.resize(self.get_size())
        return self


class Img_path(Img_conversion):
    def __init__(self, path):
        if not isinstance(path, Path):
            raise TypeError("pathにはpathlib.Pathを指定してください")
        self._path = path
        super().__init__(self._path)

    @property
    def path(self):
        return self._path


class Img_byte(Img_conversion):
    def __init__(self, byte):
        if isinstance(byte, BytesIO):
            self._bytes = byte
        if isinstance(byte, bytes):
            self._bytes = BytesIO(byte)
        elif isinstance(byte, np.bytes_):
            self._bytes = BytesIO(bytes(byte))
        elif isinstance(byte, np.ndarray) and byte.dtype.kind == "S":
            self._bytes = BytesIO(byte.tobytes())
        else:
            raise TypeError
        super().__init__(self._bytes)

    def __bytes__(self):
        return self._bytes.getvalue()

    @property
    def byte(self):
        return self._bytes.getvalue()

    @property
    def byteio(self):
        return self._bytes
