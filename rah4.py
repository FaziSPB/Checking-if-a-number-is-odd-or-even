import random
liczba = random.randint(1,10)
for i in range(3):
    liczba2 = int(input("Zgadnij liczbe: "))

    if liczba == liczba2:
        print("Brawo! Odgadles!")
        break
    elif liczba2 > liczba:
       if i < 2:
            print("Za duza, Sprobuj jeszcze raz")
    elif liczba2 < liczba:
        if i < 2:
            print("Za mala, Sprobuj jeszcze raz")
else:
    print("Nie znaleziono, poprawna liczba to", liczba)
