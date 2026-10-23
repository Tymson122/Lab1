import random

droga = random.randint(1, 500)
srednie_spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Cena paliwa za litr: "))

zuzycie = (droga / 100) * srednie_spalanie
koszt = zuzycie * cena_paliwa

print(f"Wylosowana droga: {droga} km")
print(f"Zużycie paliwa: {zuzycie:.2f} l")
print(f"Koszt podróży: {koszt:.2f} zł")