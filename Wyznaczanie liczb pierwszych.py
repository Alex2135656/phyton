def czy_pierwsza(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def wyznacz_liczby_pierwsze(limit):
   
    liczby_pierwsze = []
    for i in range(2, limit + 1):
        if czy_pierwsza(i):
            liczby_pierwsze.append(i)
    return liczby_pierwsze

limit = int(input("Podaj górną granicę przedziału: "))
wynik = wyznacz_liczby_pierwsze(limit)

print(f"Liczby pierwsze od 2 do {limit}: {wynik}")
