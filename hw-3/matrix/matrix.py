import copy
from typing import List, Union

import numpy as np


class MatrixHashMixin:
    def __hash__(self) -> int:
        # Сумма элементов, умноженная на количество строк
        return sum(sum(row) for row in self.data) * self.rows

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data


class Matrix(MatrixHashMixin):
    def __init__(self, data: List[List[Union[int, float]]]):
        if not data:
            raise ValueError("Matrix must have at least one element")
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        for row in data:
            if len(row) != self.cols:
                raise ValueError("Matrix must have same number of elements")

        self.data = data
        self._cached_mul = {}



    def _check_dimensions(self, first, second):
        if self.rows != first or self.cols != second:
            raise ValueError("Dimensions mismatch")

    def __add__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} is not a Matrix object")
        self._check_dimensions(other.rows, other.cols)
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} is not a Matrix object")
        self._check_dimensions(other.rows, other.cols)
        result = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} is not a Matrix object")
        if self.cols != other.rows:
            raise ValueError(f"Lhs columns != rhs rows: {self.cols} != {other.rows}")
        other_hash = hash(other)
        if other_hash in self._cached_mul:
            return self._cached_mul[other_hash]
        result = Matrix([
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ])

        self._cached_mul[other_hash] = result
        return result

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


# np.random.seed(0)
# matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
# matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
#
# result = matrix1 + matrix2
# result.save_to_file('matrix+.txt')
#
# result = matrix1 * matrix2
# result.save_to_file('matrix*.txt')
#
# result = matrix1 @ matrix2
# result.save_to_file('matrix@.txt')
