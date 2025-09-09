oceny_uczniow = [
    [5, 3, 2],
    [1, 4, 6],
    [2, 5, 4]
]
srednie_uczniow = []
for i, uczen in enumerate(oceny_uczniow):
    srednia = sum(uczen)/len(uczen)
    srednie_uczniow.append(srednia)
    print("Srednia ucznia", i+1, ":", srednia)


srednia_klasy = sum(srednie_uczniow)/len(srednie_uczniow)
print("Srednia klasy to: ", srednia_klasy)

print("Powyzej sredniej klasy: ")
for k, srednia in enumerate(srednie_uczniow):
    if srednia > srednia_klasy:
            print("uczen ",k+1, ":", srednia)

