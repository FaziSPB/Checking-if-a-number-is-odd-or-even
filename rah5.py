oceny = [4, 3, 2, 1, 5, 6 , 7, 8, 9]
suma = sum(oceny)
srednia = suma/len(oceny)
print("srednia ocen to: ",srednia)

powyzej = []
for ocena in oceny:
    if ocena > srednia:
        powyzej.append(ocena)
print("oceny powyzej sredniej to",powyzej)

