class WrongInputType(Exception):
    """Throw this exception when expected diffrent type."""

class OutOfRange(Exception):
    """Throw this exception when out of range."""

class WrongObjectSize(Exception):
    """Throw this exception when expected diffrent object size."""

class InvalidTransformationInput(Exception):
    """Throw this exception then invalid transformation input."""

import cmath
from Vector import *


class Matrix:

    def __init__(self, mat):
        self.__param = []
        self._proper_args(mat)
        self._round_param()

    def _proper_args(self, mat):
        if not isinstance(mat, list) or len(mat) == 0:
            raise WrongInputType
        elif not all(isinstance(row, list) and len(row) > 0 for row in mat):
            raise WrongInputType
        else:
            width = len(mat[0])
            for i in range(len(mat)):
                self.__param.append([])
                if len(mat[i]) != width:
                    raise WrongInputType
                for num in mat[i]:
                    if isinstance(num, tuple):
                        if len(num) != 2 or not isinstance(num[0], (int, float)) or not isinstance(num[0], (int, float)):
                            raise WrongInputType
                        else:
                            self.__param[i].append(complex(num[0], num[1]))
                    elif isinstance(num, (int, float, complex)):
                        self.__param[i].append(num)
                    else:
                        raise WrongInputType

    def _round_param(self):
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                self.__param[i][j] = complex(round(self.__param[i][j].real, 9), round(self.__param[i][j].imag, 9))

    @classmethod
    def identity(cls, m_size):
        if isinstance(m_size, int):
            if m_size < 1:
                raise OutOfRange
            new_matrix = []
            for i in range(m_size):
                new_matrix.append([0] * i + [1] + [0] * (m_size - i - 1))
            return Matrix(new_matrix)
        else:
            raise WrongInputType

    @classmethod
    def empty(cls, m_size):
        if isinstance(m_size, int):
            if m_size < 1:
                raise OutOfRange
            else:
                return Matrix([[0] * m_size] * m_size)
        else:
            raise WrongInputType

    @classmethod
    def from_vector(cls, vec):
        if isinstance(vec, Vector):
            new_matrix = []
            for i in range(vec.size()):
                new_matrix.append([vec[i]])
            return Matrix(new_matrix)
        else:
            raise WrongInputType

    def __str__(self):
        printable = ""
        for row in self.__param:
            printable += str(row)
            printable += "\n"
        return printable

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if len(self.__param) != len(other.__param) or len(self.__param[0]) != len(other.__param[0]):
                return False
            else:
                for i in range(len(self.__param)):
                    if not all(self.__param[i][j] == other.__param[i][j] for j in range(len(self.__param[0]))):
                        return False
                return True
        else:
            return False

    def __imul__(self, other):
        if isinstance(other, Matrix):
            if len(self.__param[0]) != len(other.__param):
                raise WrongObjectSize
            else:
                same_dim = len(self.__param[0])
                for i in range(len(self.__param)):
                    new_row = []
                    for ii in range(len(other.__param[0])):
                        new_num = 0
                        for j in range(same_dim):
                            new_num += self.__param[i][j] * other.__param[j][ii]
                        new_row.append(new_num)
                    self.__param[i] = new_row
                return self
        else:
            raise WrongInputType

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise WrongObjectSize
            else:
                same_dim = len(self.__param[0])
                new_matrix = []
                for i in range(len(self.__param)):
                    new_row = []
                    for ii in range(len(other.__param[0])):
                        new_num = 0
                        for j in range(same_dim):
                            new_num += self.__param[i][j] * other.__param[j][ii]
                        new_row.append(new_num)
                    new_matrix.append(new_row)
                return Matrix(new_matrix) 
        else:
            raise WrongInputType

    def __rmul__(self, other):
        if isinstance(other, (float, int, complex)):
            new_matrix = []
            for row in self.__param:
                new_row = []
                for num in row:
                    new_row.append(other * num)
                new_matrix.append(new_row)
            return Matrix(new_matrix)
        else:
            raise WrongInputType

    def __iadd__(self, other):
        if isinstance(other, Matrix):
            if self.size() != other.size():
                raise WrongObjectSize
            else:
                for i in range(self.size()[0]):
                    for j in range(self.size()[1]):
                        self.__param[i][j] += other.__param[i][j]
                return self
        else:
            raise WrongInputType

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.size() != other.size():
                raise WrongObjectSize
            else:
                new_matrix = []
                for row in self.__param:
                    new_matrix.append(row.copy())
                new_matrix = Matrix(new_matrix)
                new_matrix += other
                return new_matrix

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            raise WrongInputType

    def __neg__(self):
        new_matrix = []
        for row in self.__param:
            new_row = []
            for num in row:
                new_row.append(-num)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __isub__(self, other):
        if isinstance(other, Matrix):
            self += (-other)
            return self
        else:
            raise WrongInputType

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return self + (-other)
        else:
            raise WrongInputType

    def __rsub__(self, other):
        if isinstance(other, Matrix):
            return other + (-self)
        else:
            raise WrongInputType

    def __pow__(self, other):
        if isinstance(other, int):
            if self.size()[0] != self.size()[1]:
                raise WrongObjectSize
            else:
                #for now, lineral by exponent
                temp = Matrix.identity(self.size()[0])
                for i in range(other):
                    temp *= self
                return temp
        else:
            raise WrongInputType

    def __getitem__(self, key):
        if isinstance(key, int):
            if key > self.size()[0]:
                raise OutOfRange
            else:
                return self.__param[key]
        else:
            raise WrongInputType

    def size(self):
        return (len(self.__param), len(self.__param[0]))

    def __call__(self, v):
        if isinstance(v, Vector):
            if v.size() != self.size()[1]:
                raise WrongObjectSize
            else:
                new_vector = []
                for row in self.__param:
                    new_num = 0
                    for i in range(v.size()):
                        new_num += row[i] * v[i]
                    new_vector.append(new_num)
                return Vector(new_vector)

    def copy(self):
        new_matrix = []
        for row in self.__param:
            new_matrix.append(row.copy())
        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = []
        for i in range(self.size()[1]):
            new_row = []
            for j in range(self.size()[0]):
                new_row.append(self.__param[j][i])
            new_matrix.append(new_row)
        self.__param = new_matrix
        return self

    def conjugate_transpose(self):
        new_matrix = []
        for i in range(self.size()[1]):
            new_row = []
            for j in range(self.size()[0]):
                new_row.append(complex(self.__param[j][i].real, -self.__param[j][i].imag))
            new_matrix.append(new_row)
        self.__param = new_matrix
        return self

    def switch_rows(self, r1, r2):
        if isinstance(r1, int) and isinstance(r2, int):
            if r1 >= self.size()[0] or r2 >= self.size()[0]:
                raise OutOfRange
            elif r1 == r2:
                raise InvalidTransformationInput
            else:
                for i in range(self.size()[1]):
                    temp = self.__param[r1][i]
                    self.__param[r1][i] = self.__param[r2][i]
                    self.__param[r2][i] = temp
                return self
        else:
            raise WrongInputType
            
    def multiply_row(self, r1, scal):
        if isinstance(r1, int) and isinstance(scal, (int, float, complex)):
            if r1 >= self.size()[0]:
                raise OutOfRange
            elif scal == 0:
                raise InvalidTransformationInput
            else:
                for i in range(self.size()[1]):
                    self.__param[r1][i] *= scal
                return self
        else:
            raise WrongInputType

    def add_row(self, r1, r2, scal):
        if isinstance(r1, int) and isinstance(r2, int) and isinstance(scal, (int, float, complex)):
            if r1 >= self.size()[0] or r2 >= self.size()[0]:
                raise OutOfRange
            elif r1 == r2:
                raise InvalidTransformationInput
            else:
                for i in range(self.size()[1]):
                    self.__param[r1][i] += scal * self.__param[r2][i]
                return self
        else:
            raise WrongInputType

    def shuffle(self):
        for i in range(int(self.size()[0] / 2)):
            for j in range(self.size()[1]):
                temp = self.__param[i][j]
                self.__param[i][j] = self.__param[self.size()[0] - i - 1][j]
                self.__param[self.size()[0] - i - 1][j] = temp
        return self

    def attach(self, other):
        if isinstance(other, Matrix):
            if self.size()[0] == other.size()[0]:
                new_matrix = []
                for i in range(self.size()[0]):
                    self.__param[i] += other.__param[i]
                return self
            else:
                raise WrongObjectSize
        else:
            raise WrongInputType
