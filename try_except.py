
while True:
    try:
        cena = input('Wprowadz cene ')
        cena = int(cena)
        break
    except ValueError:
        print('Wartosc nie jest liczba')



wynik = cena * 2.1

print(wynik)