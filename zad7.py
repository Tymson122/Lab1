a = float(input("Podaj wspolczynnik a: "))
b = float(input("Podaj wspolczynnik b: "))

if a != 0:
    x = -b / a
    print(f"Rownanie ma jedno rozwiazanie: x = {x}")
else:
    if b == 0:
        print("Rownanie ma nieskończenie wiele rozwiązan")
    else:
        print("Rownanie nie ma rozwiazan")