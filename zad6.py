droga = float(input("Podaj pokonaną drogę: "))
srednie_spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = 6.5

zuzycie = (droga / 100) * srednie_spalanie
koszt = zuzycie * cena_paliwa
print(f"Zużycie paliwa: {zuzycie}\nKoszt: {koszt}")

