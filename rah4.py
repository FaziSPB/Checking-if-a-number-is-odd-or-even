import random
liczba = random.randint(1,10)
liczba2 = int(input("Zgadnij liczbe: "))
if liczba == liczba2:
    print("Brawo! Odgadles!")
else:
    print("Sprobuj nastepnym razem")