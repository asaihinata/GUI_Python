import numpy as np

from sgg.dev.array import _ArrayCommonMixin

__all__ = ["NPBool"]


class NPBool(_ArrayCommonMixin):
    """`np.ndarray`を継承したbool型の配列クラス"""

    _element_type = (np.bool_, np.bool)
    _default_dtype = np.bool_

    def __new__(cls, obj, /, dtype=None, *, copy=True):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(obj, dtype=cls._default_dtype, copy=copy).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
            obj = np.asarray(obj, dtype=resolved, copy=copy).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        return obj

    def __invert__(self):
        result = np.asarray(np.logical_not(self)).view(type(self))
        result._dtype = self.dtypes
        return result

    __not__ = __invert__

    def __eq__(self, value):
        result = np.asarray(np.equal(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    def __ne__(self, value):
        result = np.asarray(np.not_equal(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def TrueCount(self):
        return int(np.count_nonzero(self))

    @property
    def FalseCount(self):
        return int(np.count_nonzero(~self))

    def all(self):
        return bool(np.all(np.asarray(self)))

    def any(self):
        return bool(np.any(np.asarray(self)))

    def inversion(self):
        result = np.asarray(np.logical_not(self)).view(type(self))
        result._dtype = self.dtypes
        return result
