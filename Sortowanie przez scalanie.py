def merge_sort(tab):
    if len(tab) <= 1:
        return tab

    s = len(tab) // 2
    lewa = merge_sort(tab[:s])
    prawa = merge_sort(tab[s:])

    wynik = []
    i = j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i]); i += 1
        else:
            wynik.append(prawa[j]); j += 1

    wynik += lewa[i:]
    wynik += prawa[j:]

    return wynik


dane = [5, 2, 9, 1, 3, 7]

print("Przed:", dane)
print("Po:", merge_sort(dane))