import random

slowa = ["kot", "pies", "malina", "python", "domek"]
wisielec = random.choice(slowa)

stan_slowo = ["_"] * len(wisielec)
zycia = 6
while zycia > 0 and "_" in stan_slowo :
    litera = input("Podaj litere: ")
    if litera in wisielec:
        for i in range(len(wisielec)):
            if litera == wisielec[i]:
                stan_slowo[i] = litera
        print("Dobrze,", stan_slowo )
    else:
        zycia -= 1
        print("Zlee! Pozostalo prob:", zycia)
if "_" not in stan_slowo:
    print("Brawo! Odgadłeś słowo:", wisielec)
else:
    print("Koniec gry! Słowo to:", wisielec)
