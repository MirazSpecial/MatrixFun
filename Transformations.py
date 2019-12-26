class NotInvertible(Exception):
    """Throw this exception when Matrix is not invertible."""


from Matrix import *


def steps_to_triangular(mat_1):
    """Steps needed to transform given Matrix to upper triangular Matrix."""

    result = []

    #get_non_zero_under checks if there is a non-zero number in given column, equal or lower then given row, returns (true, row number) or (false, -1) 
    def get_non_zero_under(mat_0, row, column):
        while row < mat_0.size()[0]:
            if mat_0[row][column] != 0:
                return (True, row)
            else:
                row += 1
        return (False, -1) 

    #getting zeros under diagonal
    for i in range(min(mat_1.size())):
        (is_nonz, where_nonz) = get_non_zero_under(mat_1, i, i)
        if is_nonz:
            if i != where_nonz:
                mat_1.switch_rows(i, where_nonz)
                result.append(("switch", i, where_nonz))
            for j in range(i + 1, mat_1.size()[0]):
                scalar = -(mat_1[j][i] / mat_1[i][i])
                if scalar != 0:
                    mat_1.add_row(j, i, scalar)
                    result.append(("add", j, i, scalar))
    return result


def steps_to_identity(mat_1):
    """Returns steps needed to transform given Matrix to identity Matrix or raising exception if impossible."""

    if mat_1.size()[0] != mat_1.size()[1]:
        raise WrongObjectSize
    
    result = []

    #get_non_zero_under checks if there is a non-zero number in given column, equal or lower then given row, returns (true, row number) or (false, -1) 
    def get_non_zero_under(mat_0, row, column):
        while row < mat_0.size()[0]:
            if mat_0[row][column] != 0:
                return (True, row)
            else:
                row += 1
        return (False, -1) 

    #get_non_zero_above checks if there is a non-zero number in a given column, equal or higher then given row, returns (true, row number) of (false, -1)
    def get_non_zero_above(mat_0, row, column):
        while row >= 0:
            if mat_0[row][column] != 0:
                return (True, row)
            else:
                row -= 1
        return (False, -1)             

    #getting zeros under diagonal
    for i in range(mat_1.size()[0]):
        (is_nonz, where_nonz) = get_non_zero_under(mat_1, i, i)
        if is_nonz:
            if i != where_nonz:
                mat_1.switch_rows(i, where_nonz)
                result.append(("switch", i, where_nonz))
            for j in range(i + 1, mat_1.size()[0]):
                scalar = -(mat_1[j][i] / mat_1[i][i])
                if scalar != 0:
                    mat_1.add_row(j, i, scalar)
                    result.append(("add", j, i, scalar))
        else: 
            raise NotInvertible

    #getting zeros above diagonal
    for i in range(mat_1.size()[0] - 1, -1, -1):
        (is_nonz, where_nonz) = get_non_zero_above(mat_1, i, i)
        if is_nonz:
            if i != where_nonz:
                mat_1.switch_rows(i, where_nonz)
                result.append(("switch", i, where_nonz))
            for j in range(0, i):
                scalar = -(mat_1[j][i] / mat_1[i][i])
                if scalar != 0:
                    mat_1.add_row(j, i, scalar)
                    result.append(("add", j, i, scalar))
        else: 
            raise NotInvertible

    #getting ones on diagonal
    for i in range(mat_1.size()[0]):
        if mat_1[i][i] != 0:
            if mat_1[i][i] != 1:
                scalar = 1 / mat_1[i][i]
                mat_1.multiply_row(i, scalar)
                result.append(("multiply", i, scalar))
        else:
            raise NotInvertible

    return result


def follow_transformations(mat_1, trans):
    """Returns given Matrix after aplying transformations in a given list."""
    for step in trans:
        if step[0] == "switch":
            mat_1.switch_rows(step[1], step[2])
        elif step[0] == "multiply":
            mat_1.multiply_row(step[1], step[2])
        elif step[0] == "add":
            mat_1.add_row(step[1], step[2], step[3])
    return mat_1


def det(mat_1):
    """Returns determinant of given Matrix."""
    if mat_1.size()[0] != mat_1.size()[1]:
        raise WrongObjectSize
    mat_2 = mat_1.copy()
    steps = steps_to_triangular(mat_2)
    result = 1
    for step in steps:
        if step[0] == "switch":
            result *= -1
        elif step[0] == "multiply":
            result *= step[2]
    for i in range(mat_2.size()[0]):
        result *= mat_2[i][i]
    return result


def invertible(mat_1):
    """Returns invertible Matrix of given Matrix."""
    if mat_1.size()[0] != mat_1.size()[1]:
        raise WrongObjectSize
    steps = steps_to_identity(mat_1.copy())
    inver = Matrix.identity(mat_1.size()[0])
    return follow_transformations(inver, steps)


def rank(mat_1):
    """Returns rang of given Matrix."""
    mat_2 = mat_1.copy()
    steps_to_triangular(mat_2)
    result = 0
    for i in range(mat_1.size()[0]):
        if mat_2[i] != ([0] * mat_1.size()[1]):
            result += 1
    return result
