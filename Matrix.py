class WrongMatrixConstructor(Exception):
    """Throw this exception when Matrix is constructed the wrong way."""

class InvalidOperandError(Exception):
    """Throw this exception when Invalid Operand."""

class WrongObjectSize(Exception):
    """Throw this exception when an operation cannot performed."""

class OutOfRange(Exception):
    """Throw this exception when Vector size is to small."""

class WrongVectorConstructor(Exception):
    """Throw this exception when Vector is construceted in the wrong way."""

class WrongTransformationInput(Exception):
    """Throw this exception when Input to a transformation is wrong."""


class Matrix:

    def __init__(self, *args):
        if self._proper_args(args):
            self.__param = args[0]
        else:
            raise WrongMatrixConstructor

    def _proper_args(self, args):
        if not args or len(args) > 1:
            return False
        args = args[0]    
        if not isinstance(args, list) or len(args) == 0:
            return False
        elif not all(isinstance(row, list) and len(row) > 0 for row in args):
            return False
        else:
            width = len(args[0])
            for row in args:
                if len(row) != width:
                    return False
                for num in row:
                    if not isinstance(num, (int, float)):
                        return False
            return True 

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
            raise InvalidOperandError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.__param[0]) != len(other.__param):
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
            raise InvalidOperandError

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            new_matrix = []
            for row in self.__param:
                new_row = []
                for num in row:
                    new_row.append(other * num)
                new_matrix.append(new_row)
            return Matrix(new_matrix)
        else:
            raise InvalidOperandError

    def __iadd__(self, other):
        if isinstance(other, Matrix):
            if len(self.__param) != len(other.__param) or len(self.__param[0]) != len(other.__param[0]):
                raise WrongObjectSize
            else:
                for i in range(len(self.__param)):
                    for j in range(len(other.__param)):
                        self.__param[i][j] += other.__param[i][j]
                return self
        else:
            raise InvalidOperandError

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.__param) != len(other.__param) or len(self.__param[0]) != len(other.__param[0]):
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
            raise InvalidOperandError

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
            raise InvalidOperandError

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return self + (-other)
        else:
            raise InvalidOperandError

    def __rsub__(self, other):
        if isinstance(other, Matrix):
            return other + (-self)
        else:
            raise InvalidOperandError

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
                        new_num += row[i] * v(i + 1)
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
        return Matrix(new_matrix)

    def switch_rows(self, r1, r2):
        if isinstance(r1, int) and isinstance(r2, int):
            if r1 > self.size()[0] or r2 > self.size()[0]:
                raise WrongTransformationInput
            else:
                new_matrix = self.copy()
                new_matrix.__param[r1 - 1] = self.__param[r2 - 1].copy()
                new_matrix.__param[r2 - 1] = self.__param[r1 - 1].copy()
                return new_matrix
        else:
            raise WrongTransformationInput
            
    def multiply_row(self, r1, scal):
        if isinstance(r1, int) and isinstance(scal, (int, float)):
            if r1 > self.size()[0]:
                raise WrongTransformationInput
            elif scal == 0:
                raise WrongTransformationInput
            else:
                new_matrix = self.copy()
                for i in range(self.size()[1]):
                    new_matrix.__param[r1 - 1][i] *= scal
                return new_matrix
        else:
            raise WrongTransformationInput

    def add_row(self, r1, r2, scal):
        if isinstance(r1, int) and isinstance(r2, int) and isinstance(scal, (int, float)):
            if r1 > self.size()[0] or r2 > self.size()[0] or r1 == r2:
                raise WrongTransformationInput
            else:
                new_matrix = self.copy()
                for i in range(self.size()[1]):
                    new_matrix.__param[r1 - 1][i] += scal * new_matrix.__param[r2 - 1][i]
                return new_matrix
        else:
            raise WrongTransformationInput



class Vector:
    
    def __init__(self, *args):
        if self._proper_args(args):
            self.__param = args[0]
        else:
            raise WrongVectorConstructor

    def _proper_args(self, args):
        if not args or len(args) > 1:
            return False
        args = args[0]    
        if not isinstance(args, list) or len(args) == 0:
            return False
        else:
            for num in args:
                if not isinstance(num, (int, float)):
                    return False
            return True

    def __str__(self):
        return(str(self.__param))

    def __eq__(self, other):
        if not isinstance(other, Vector) or len(self.__param) != len(other.__param):
            return False
        else:
            if all(self.__param[i] == other.__param[i] for i in range(len(self.__param))):
                return True
            else:
                return False

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self.__param) != len(other.__param):
                raise WrongObjectSize
            else:
                for i in range(len(self.__param)):
                    self.__param[i] += other.__param[i]
                return self
        else:
            raise InvalidOperandError

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.__param) != len(other.__param):
                raise WrongObjectSize
            else:
                new_vector = Vector(self.__param.copy())
                new_vector += other
                return new_vector
        else:
            raise InvalidOperandError

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        else:
            raise InvalidOperandError

    def __mul__(self, other):
        if False:
            pass
        else:
            raise InvalidOperandError

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            new_vector = []
            for num in self.__param:
                new_vector.append(other * num)
            return Vector(new_vector)
        else:
            raise InvalidOperandError

    def __neg__(self):
        new_vector = []
        for num in self.__param:
            new_vector.append(-num)
        return Vector(new_vector)

    def __isub__(self, other):
        if isinstance(other, Vector):
            self += (-other)
            return self
        else:
            raise InvalidOperandError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self + (-other)
        else:
            raise InvalidOperandError

    def  __rsub__(self, other):
        if isinstance(other, Vector):
            return other + (-self)
        else:
            raise InvalidOperandError

    def __call__(self, other):
        if isinstance(other, int):
            if other > len(self.__param):
                raise OutOfRange
            else:
                return self.__param[other - 1]
        else:
            raise InvalidOperandError

    def size(self):
        return len(self.__param)

    def copy(self):
        return Vector(self.__param.copy())