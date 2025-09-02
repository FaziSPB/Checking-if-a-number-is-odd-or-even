liczba = int(input("Podaj liczbe: "))

# sprawdzenie znaku
if liczba >0:
    print("Liczba jest dodatnia!")
elif liczba <0:
    print("Liczba jest ujemna!")
else: print("liczba to 0")

# sprawdzenie podzielnosci


if liczba % 2 == 0 or liczba % 3 == 0 or liczba % 5 == 0:
    if liczba % 2 == 0:print("liczba jest podzielna przez 2")
    if liczba % 3 == 0:print("liczba jest podzielna przez 3")
    if liczba % 5 == 0:print("liczba jest podzielna przez 5")
else: print("liczba nie jest podzielna ani przez 2,3 ani 5")