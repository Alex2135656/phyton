def na_binarny(n):
    wynik = ""

    while n > 0:
        reszta = n % 2
        wynik = str(reszta) + wynik
        n = n // 2

    return wynik


liczba = 13

print("Liczba dziesiętna:", liczba)
print("Liczba binarna:", na_binarny(liczba))