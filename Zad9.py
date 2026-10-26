a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))

print(f"Suma = {a + b}")
print(f"Roznica = {a - b}")
print(f"Iloczyn = {a * b}")
if b == 0:
    print("Wynik dzielenia: Blad!")
else:
    print(f"Iloraz = {a / b}")

print(f"Potega = {a ** b}")