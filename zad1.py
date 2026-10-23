# ZAD 1A

# 1. dodawanie dwóch int -> int
print(1 + 2, type(1 + 2))          # 3, <class 'int'>

# 2. int + float -> float
print(1 + 4.5, type(1 + 4.5))      # 5.5, <class 'float'>

# 3. / dzielenie zmiennoprzecinkowe, zawsze zwraca float
print(3 / 2, type(3 / 2))          # 1.5, <class 'float'>

# 4. nawet gdy wynik jest równy, / daje float
print(4 / 2, type(4 / 2))          # 2.0, <class 'float'>

# 5. // dzielenie całkowite
print(3 // 2, type(3 // 2))        # 1, <class 'int'>

# 6. // zaokrągla w dół
print(-3 // 2, type(-3 // 2))      # -2, <class 'int'>

# 7. % reszta z dzielenia (modulo)
print(11 % 2, type(11 % 2))        # 1, <class 'int'>

# 8. ** potęgowanie
print(2 ** 10, type(2 ** 10))      # 1024, <class 'int'>

# 9. potęga ułamkowa = pierwiastek
print(8 ** (1/3), type(8 ** (1/3)))  # 2.0, <class 'float'>

# ZAD 1B
int(3.0)    #  float na int
float(3)    #  int na float
float("3")  # tekst (str) na float
str(12.4)   # float na tekst
bool(0)     # 0 = Fałsz, inna liczba to True