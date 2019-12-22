import unittest


class TestsMatrix(unittest.TestCase):
    """Main Matrix test class"""

    #raising Exception when constructiong Matrix from wrong input
    def test_1_1(self):
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[1, "a"]])
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[]])
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([])
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix()
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[1], "a"])
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[1]], [[1]])

    #raising Exception when constructing Matrix from diffrent sized rows
    def test_1_2(self):
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[1, 2, 3], [2, 3]])
        with self.assertRaises(WrongMatrixConstructor):
            moja_macierz = Matrix([[1, 2], [1, 2, 3]])
    
    #multiplying number and matrix and raising Exception when multiplying matrix and number
    def test_2_1(self):
        assert 2 * Matrix([[1, 1], [1, 1]]) == Matrix([[2, 2], [2, 2]])
        assert 0 * Matrix([[2, 2], [2, 2]]) == Matrix([[0, 0], [0, 0]])
        with self.assertRaises(InvalidOperandError):
            Matrix([[1]]) * 0

    #multiplying matrix and matrix (and imul)
    def test_2_3(self):
        macierz_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        macierz_2 = Matrix([[2], [2], [2]])
        macierz_3 = Matrix([[12], [30]])
        macierz_4 = Matrix([[2, 3]])
        macierz_5 = Matrix([[14, 19, 24]])
        assert macierz_1 * macierz_2 == macierz_3
        assert macierz_4 * macierz_1 == macierz_5
        with self.assertRaises(InvalidOperandError):
            macierz_4 * [[1]]
        with self.assertRaises(WrongObjectSize):
            macierz_2 * macierz_1
        with self.assertRaises(WrongObjectSize):
            macierz_4 * macierz_2
        macierz_4 *= macierz_1
        macierz_4 *= macierz_2
        assert macierz_4 == Matrix([[114]])

    #adding or substracting matrix and matrix
    def test_2_4(self):
        macierz_1 = Matrix([[1]])
        macierz_2 = Matrix([[2]])
        assert macierz_1 + macierz_1 == macierz_2
        macierz_1 += macierz_1
        assert macierz_1 == macierz_2
        macierz_3 = Matrix([[1, 2], [3, 4]])
        macierz_4 = Matrix([[0.1, 0.3], [0.5, 9.7]])
        assert macierz_3 + macierz_4 == macierz_4 + macierz_3
        assert macierz_3 + macierz_4 == Matrix([[1.1, 2.3], [3.5, 13.7]])
        macierz_1 = 0.5 * macierz_1
        assert macierz_2 - macierz_1 == macierz_1
        macierz_2 -= macierz_1
        assert macierz_1 == macierz_2

    #calling Matrix as a function
    def test_3_1(self):
        macierz_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        wektor_1 = Vector([2, 2, 2])
        assert macierz_1(wektor_1) == Vector([12, 30])
        assert macierz_1(Vector([0, 0, 0])) == Vector([0, 0])
        with self.assertRaises(WrongObjectSize):
            macierz_1(Vector([0]))

    #Matrix transposition
    def test_3_2(self): 
        macierz_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        macierz_2 = Matrix([[1, 4], [2, 5], [3, 6]])
        macierz_3 = Matrix([[1, 2, 3, 4, 5]])
        macierz_4 = Matrix([[1], [2], [3], [4], [5]])
        macierz_5 = Matrix([[1]])
        assert macierz_1.transpose() == macierz_2
        assert macierz_2.transpose() == macierz_1
        assert macierz_3.transpose() == macierz_4
        assert macierz_4.transpose() == macierz_3
        assert macierz_5.transpose() == macierz_5

    #Matrix elementary transformation - switching rows
    def test_4_1(self):
        macierz_1 = Matrix([[1, 2], [3, 4], [5, 6]])
        macierz_2 = Matrix([[3, 4], [5, 6], [1, 2]])
        macierz_3 = Matrix([[5, 6], [3, 4], [1, 2]])
        assert macierz_1.switch_rows(1, 3) == macierz_3
        assert macierz_1.switch_rows(3, 1) == macierz_3
        assert macierz_3.switch_rows(1, 3) == macierz_1
        assert macierz_3.switch_rows(3, 1) == macierz_1
        assert macierz_3.switch_rows(1, 2) == macierz_2
        assert macierz_2.switch_rows(2, 2) == macierz_2
        with self.assertRaises(WrongTransformationInput):
            macierz_1.switch_rows(1, "a")
        with self.assertRaises(WrongTransformationInput):
            macierz_1.switch_rows(1, 4)

    #Matrix elementary transformation - multiplying row by scalar
    def test_4_2(self):
        macierz_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        macierz_2 = Matrix([[2, 4, 6], [4, 5, 6]])
        macierz_3 = Matrix([[1, 2, 3], [2, 2.5, 3]])
        assert macierz_1.multiply_row(1, 2) == macierz_2
        assert macierz_1.multiply_row(2, 0.5) == macierz_3
        with self.assertRaises(WrongTransformationInput):
            macierz_1.multiply_row(1, 0)
        with self.assertRaises(WrongTransformationInput):
            macierz_1.multiply_row(3, 1)

    #Matrix elementary transformation - adding row multiplyed by scalar
    def test_4_3(self):
        macierz_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        macierz_2 = Matrix([[5, 7, 9], [4, 5, 6]])
        macierz_3 = Matrix([[3, 4.5, 6], [4, 5, 6]])
        assert macierz_1.add_row(1, 2, 1) == macierz_2
        assert macierz_1.add_row(1, 2, 0.5) == macierz_3
        with self.assertRaises(WrongTransformationInput):
            macierz_1.add_row(1, 1, 1)
        with self.assertRaises(WrongTransformationInput):
            macierz_1.add_row(3, 1, 1)

class TestsVector(unittest.TestCase):
    """Main Vector test class"""

    #raising exception when constuctiong Vector from wrong input
    def testV_1(self):
        with self.assertRaises(WrongVectorConstructor):
            moj_wektor = Vector([1, "a"])
        with self.assertRaises(WrongVectorConstructor):
            moj_wektor = Vector([])
        with self.assertRaises(WrongVectorConstructor):
            moj_wektor = Vector()
        with self.assertRaises(WrongVectorConstructor):
            moj_wektor = Vector([1], [1])
    
    #basic Vector operations (+, -, *, size, ==)
    def testyV_2(self):
        wektor_1 = Vector([1, 2, 3])
        wektor_2 = Vector([4, 5, 6])
        wektor_3 = Vector([2, 4, 6])
        wektor_4 = Vector([5, 7, 9])
        wektor_5 = Vector([1, 2])
        assert wektor_1 == wektor_1
        assert wektor_1 != wektor_2
        assert 2 * wektor_1 == wektor_3
        assert wektor_1 + wektor_2 == wektor_4
        assert wektor_2 + wektor_1 == wektor_4
        with self.assertRaises(WrongObjectSize):
            wektor_1 + wektor_5
        with self.assertRaises(InvalidOperandError):
            wektor_5 + [0, 0]
        wektor_1 += wektor_2
        assert wektor_1 == wektor_4
        wektor_1 -= wektor_2
        assert 2 * wektor_1 == wektor_3
        assert wektor_4 - wektor_1 == wektor_2
        assert wektor_4 - wektor_2 == wektor_1
        with self.assertRaises(InvalidOperandError):
            wektor_5 - [0, 0]
        with self.assertRaises(WrongObjectSize):
            wektor_2 -= wektor_5
        with self.assertRaises(WrongObjectSize):
            wektor_1 - wektor_5


unittest.main()