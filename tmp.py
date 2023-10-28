
while True:
    try:
        num1 = float(input('Podaj liczbe 1: '))
        num2 = float(input('Podaj liczbe 2: '))
        break
    except ValueError:
        print('Podano niewlasciwa wartosc')


try:
    result = num1/num2
    print(f'Wynik dzielenia to: {result}')
except ZeroDivisionError:
    result = 0
    print('Dzielenie sie nie powiodlo: result = 0')


print('Dalsza czesc programu')