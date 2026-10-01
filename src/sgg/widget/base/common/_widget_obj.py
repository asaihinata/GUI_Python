from tkinter import TclError
import numpy as np
__all__=["_WIDGET_OBJ"]
class _WIDGET_OBJ:
    def _nums(self, val, other=None):
        return val if self._is_number(val) else other

    def _num0s(self, val, mins=0):
        return val if self._is_number(val) and 0 <= val else mins

    def _num0(self, val, mins=0):
        return val if self._is_number(val) and 0 < val else mins

    def _bols(self, j, o=True):
        if isinstance(j, bool) or (isinstance(j, np.generic) and j.dtype.kind == "b"):
            return j
        return o

    def _to_str(self, s):
        if isinstance(s, str):
            return s
        if isinstance(s, np.str_):
            return str(s)

    def _is_str(self, s):
        if isinstance(s, str) or (
            isinstance(s, np.generic) and np.issubdtype(s.dtype, np.str_)
        ):
            return True
        return False

    def _to_number(self, val):
        if isinstance(val, int | np.integer):
            return int(val)
        elif isinstance(val, float | np.floating):
            return float(val)
        elif isinstance(val, complex | np.complexfloating):
            return complex(val)

    def _is_number(self, val):
        if isinstance(val, int | float | complex) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.number)
        ):
            return True
        return False

    def _is_real(self, val):
        if isinstance(val, int | float) or (
            isinstance(val, np.generic)
            and np.issubdtype(val.dtype, np.integer | np.floating)
        ):
            return True
        return False

    def _to_real(self, val):
        if isinstance(val, int | float):
            return val
        elif isinstance(val, np.generic):
            if np.issubdtype(val.dtype, np.integer):
                return int(val)
            elif np.issubdtype(val.dtype, np.floating):
                return float(val)

    def _is_int(self, val):
        if isinstance(val, int) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.integer)
        ):
            return True
        return False

    def _is_float(self, val):
        if isinstance(val, float) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.floating)
        ):
            return True
        return False

    def _up0s(self, val, min):
        return val if self._is_real(val) and 0 <= val else min

    def _to_str_flat_list(self, array):
        if isinstance(array, list | tuple):
            return self._flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray) and array.dtype.kind == "U":
            return array.ravel().tolist()
        elif isinstance(array, str):
            return [array]
        elif isinstance(array, np.str_):
            return [str(array)]
        raise TypeError(f"{array}には文字列のみが入った配列を指定してください")

    def _to_flat_list(self, array):
        if np.isscalar(array):
            return [array]
        elif isinstance(array, list | tuple):
            return self._flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray):
            return array.ravel().tolist()

    def _flatten(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list | tuple):
                result.extend(self._flatten(item))
            else:
                result.append(item)
        return result

    def _listchose(self, val, arr, other=None):
        if val in arr:
            return val
        elif other is None:
            return arr[0]
        return other

    def _fpixels(self, val):
        try:
            return self.root.winfo_fpixels(val)
        except TclError:
            raise ValueError(f"{val}が不正の値です")
        except Exception as e:
            raise Exception(e)

    def _dwh(self, val, other=None):
        try:
            return self._fpixels(val)
        except:
            return other

    def _dwh_int(self, val, other=None):
        if isinstance(val, int) and 0 <= val:
            return val
        return other
