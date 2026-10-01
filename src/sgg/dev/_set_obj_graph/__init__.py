import numpy as np

from sgg.dev._set_obj import _SET_OBJ

__all__ = ["_SET_OBJ_GRAPH"]


class _SET_OBJ_GRAPH(_SET_OBJ):
    def _range_num(self, val, mins, maxs, others=None):
        if mins <= val <= maxs:
            return val
        return others

    def _list_loop(self, lin, num):
        if not isinstance(lin, np.ndarray | list | tuple):
            lin = np.array([lin])
        if not isinstance(num, int):
            num = 0
        return np.tile(lin, int(np.ceil(num / len(lin))))[:num]

    def _tonparray(self, data, *, ndmin=0, ndmax=0):
        if isinstance(data, list | tuple | range):
            kwargs = {}
            if ndmin:
                kwargs["ndmin"] = ndmin
            if ndmax:
                kwargs["ndmax"] = ndmax
            data = np.array(data, **kwargs)
        elif hasattr(data, "__array__"):
            data = data.__array__()
            l = data.ndim
            if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
                raise TypeError
        elif isinstance(data, np.ndarray):
            l = data.ndim
            if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
                raise TypeError
        else:
            raise TypeError
        if isinstance(data, np.ndarray) and data.dtype.kind == "M":
            return np.datetime_as_string(data)
        return data

    def _change_array_like(self, obj):
        if (isinstance(obj, np.ndarray) and 1 <= obj.ndim) or isinstance(
            obj, list | tuple | range
        ):
            return True
        elif np.isscalar(obj):
            return True
        elif hasattr(obj, "__array__"):
            return True
        return False

    def _num1s(self, val, mins=1):
        return val if self._is_real(val) and 1 <= val else mins
