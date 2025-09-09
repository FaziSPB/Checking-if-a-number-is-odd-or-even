import random
punkty = 0
for i in range(5):
    liczba1 = random.randint(1,10)
    liczba2 = random.randint(1,10)
    wynik = liczba1 * liczba2
    odpowiedz = int(input(f"Ile to jest {liczba1}x{liczba2}?: "))
    if odpowiedz == wynik:
        punkty = punkty + 1
        if i<5: print("Dobra odpowiedz, oto nastepne pytanie:")
        else: print ("Dobra odpowiedz!")
    else:
        if i<5: print("Zla odpowiedz, oto nastepne pytanie:")
        else: print ("Zla odpowiedz!")
print("Oto zebrana liczba punktow:",punkty)


