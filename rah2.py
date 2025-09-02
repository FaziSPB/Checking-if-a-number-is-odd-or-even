liczba = int(input("Podaj liczbe: "))
if liczba % 3 == 0 and liczba % 5 == 0:
    print("Liczba podzielna przez 3 i 5")
elif liczba % 3 == 0:
    print("Liczba podzielna przez 3")
elif liczba % 5 == 0:
    print("Liczba podzielna przez 5")
else:
    print("Liczba nie jest podzielna przez 5 ani 3")

