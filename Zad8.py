import math

a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))
c = float(input("Podaj liczbe c: "))

if a == 0:
    print("To nie jest rownanie kwadratowe")
    if b != 0:
        print(f"Rozwiązanie liniowe: x = {-c / b}")
    elif c == 0:
        print("Nieskończenie wiele rozwiazan")
    else:
        print("Brak rozwiazan")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Dwa rozwiazania x1: {x1} x2: {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"x = {x}")
    else:
        print("Brak rozwiazan")