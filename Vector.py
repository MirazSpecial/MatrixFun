class WrongInputType(Exception):
    """Throw this exception when expected diffrent type."""

class OutOfRange(Exception):
    """Throw this exception when out of range."""

class WrongObjectSize(Exception):
    """Throw this exception when expected diffrent object size."""

class Vector:
    
    def __init__(self, *args):
        if self._proper_args(args):
            self.__param = args[0]
        else:
            raise WrongInputType

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

    @classmethod
    def unit(cls, v_size, number):
        if not isinstance(v_size, int) or not isinstance(number, int):
            raise WrongInputType
        else:
            if v_size < 1 or v_size <= number:
                raise OutOfRange
            else:
                return cls([0] * number + [1] + [0] * (v_size - number - 1))

    @classmethod
    def empty(cls, v_size):
        if not isinstance(v_size, int):
            raise WrongInputType
        else:
            return Vector([0] * v_size)

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
            raise WrongInputType

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.__param) != len(other.__param):
                raise WrongObjectSize
            else:
                new_vector = Vector(self.__param.copy())
                new_vector += other
                return new_vector
        else:
            raise WrongInputType

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        else:
            raise WrongInputType

    def __mul__(self, other):
        if False:
            pass
        else:
            raise WrongInputType

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            new_vector = []
            for num in self.__param:
                new_vector.append(other * num)
            return Vector(new_vector)
        else:
            raise WrongInputType

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
            raise WrongInputType

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self + (-other)
        else:
            raise WrongInputType

    def  __rsub__(self, other):
        if isinstance(other, Vector):
            return other + (-self)
        else:
            raise WrongInputType

    def __getitem__(self, key):
        if isinstance(key, int):
            if key > self.size():
                raise OutOfRange
            else:
                return self.__param[key]
        else:
            raise WrongInputType

    def reverse(self):
        new_vector = self.__param.copy()
        new_vector.reverse()
        return Vector(new_vector)

    def size(self):
        return len(self.__param)

    def copy(self):
        return Vector(self.__param.copy())