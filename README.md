# MatrixFun
Tworzenie macierzy: 
```
moja_macierz = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 5, 7, 9]])
```
Tworzenie wektora:
```
moj_wektor = Vector([1, 2, 3, 4])
```
Operacje zdefiniowane na macierzach: dodawanie, odejmowanie, mnożenie przez skalar i przez macierz, wypisanie (print(moja_macierz)), wywołanie macierzy jako przekształcenia z parametrem wektora (moja_macierz(moj_wektor)), wypisanie rozmiarów (.size()), stworzenie kopii (.copy()), oraz operacje elementarne na macierzy w następującej postaci
```
moja_macierz.switch_rows(1, 2) #zamienianie wierszy o podanych numerach
moja_macierz.multiply_row(3, 2.5) #mnożenie podanego wiersza przez podany skalar
moje_macierz.add_row(2, 1, 0.5) #dodanie do podanego wiersza innego wiersza pomnożonoego przez skalar
```
Oprócz tego zdefiniowana jest jeszcze garść podstawowych operacji na wektorach.
