# MatrixFun
Creating matrix:
```
my_matrix = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 5, 7, 9]])
my_matrix = Matrix([[(1, 2), (0, 1), 2], [(0, -2), 3, 4]]) #where (a, b) symbolizes complex number a+bi
```
Crearing vector:
```
my_vector = Vector([1, 2, 3, 4])
```
Defined matrix operations: adding, subtracting, multiplying by scalar and multiplying by another matrix, raising square matrix
to natural power, printing it, transposition, conjugate transposition, joining two matricies, using matrix to linear map a vector, and 
all elementary row operations with following format:
```
my_matrix.switch_rows(0, 2) 
my_matrix.multiply_row(2, 2.5) 
my_matrix.add_row(0, 1, 0.5) 
```

In the `Transformations.py` file tgere are following functions:
```
det(my_matrix) #Returns my_matrix determinant
invertible(my_matrix) #Returns invertible matrix
rank(my_matrix) #Returns my_matrix rank
```
