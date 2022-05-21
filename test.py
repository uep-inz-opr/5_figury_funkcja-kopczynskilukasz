from cmath import sqrt
import math

def pole_figury(x):
    if len(x) == 1:
        wynik = math.pi*x[0]*x[0]
        wynik = round(wynik, 2)
    elif len(x) == 2:
        wynik = x[0]*x[1]
        wynik = round(wynik, 2)
    elif len(x) == 3:
        s = (x[0] + x[1] + x[2])/2
        wynik = math.sqrt(s*(s - x[0]) * (s - x[1]) * (s - x[2]))
        wynik = round(wynik, 2)
    else:
        return "Error!! You can put only 3 characters"
    return wynik

pole=0
liczba_figur = input()
liczba_figur = int(liczba_figur)

for i in range(liczba_figur):
    figura = input().strip()
    figura = figura.split(' ')
    for j in range(len(figura)):
        figura[j] = float(figura[j])

    wynik_funkcji = pole_figury(figura)
    if type(wynik_funkcji) is not float:
        pole = wynik_funkcji
        break
    pole = pole + wynik_funkcji
    pole = round(pole, 2)

print(pole)
