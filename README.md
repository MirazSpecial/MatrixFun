# MatrixFun
Tworzenie macierzy: 
```
moja_macierz = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 5, 7, 9]])
moja_macierz = Matrix([[(1, 2), (0, 1), 2], [(0, -2), 3, 4]]) #gdzie (a, b) oznacza liczbę zespoloną a+bi
```
Tworzenie wektora:
```
moj_wektor = Vector([1, 2, 3, 4])
```
Operacje zdefiniowane na macierzach: dodawanie, odejmowanie, mnożenie przez skalar i przez macierz, podnoszenie kwadratowej macierzy do potęgi naturalnej, wypisanie (print(moja_macierz)), transpozycja, sprzężenie hermiowskie, sklejenie (doklejenie do prawej strony macierzy innej macierzy), wywołanie macierzy jako przekształcenia z parametrem wektora (moja_macierz(moj_wektor)), wypisanie rozmiarów (.size()), stworzenie kopii (.copy()), oraz operacje elementarne na macierzy w następującej postaci. 
```
moja_macierz.switch_rows(0, 2) #zamienianie wierszy o podanych numerach
moja_macierz.multiply_row(2, 2.5) #mnożenie podanego wiersza przez podany skalar
moje_macierz.add_row(0, 1, 0.5) #dodanie do podanego wiersza innego wiersza pomnożonoego przez skalar
```
Oprócz tego zdefiniowana jest jeszcze garść podstawowych operacji na wektorach.

W pliku Transformations.py dostępne są funkcje:
```
det(moja_macierz)
invertible(moja_macierz)
rank(moja_macierz)
```
zwracające odpowiednio: wyznacznik podanej macierzy, macierz odwrotną do danej macierzy i rząd danej macierzy.
