from typing import Union, List

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class SaveToFileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class PrettyMixin:
    def __str__(self):
        return np.array_str(self._data, precision=2)


class NpMatrix(NDArrayOperatorsMixin, SaveToFileMixin, PrettyMixin):
    def __init__(self, data: List[List[Union[int, float]]]):
        if not data or len(data) == 0:
            raise ValueError("Matrix must have at least one element")
        self._rows = len(data)
        self._cols = len(data[0]) if self._rows > 0 else 0
        for row in data:
            if len(row) != self._cols:
                raise ValueError("Matrix must have same number of elements")
        self._data = np.array(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = []
        for input in inputs:
            if isinstance(input, NpMatrix):
                args.append(input._data)
            else:
                args.append(input)
        result = getattr(ufunc, method)(*args, **kwargs)
        return NpMatrix(result.tolist()) if isinstance(result, np.ndarray) else result

    @property
    def data(self) -> np.ndarray:
        return self._data

    @data.setter
    def data(self, new_data):
        new_matrix = NpMatrix(new_data)
        self._data = new_matrix.data
        self._rows = new_matrix.rows
        self._cols = new_matrix.cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols
