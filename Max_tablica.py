tab = [4, 6, 2, 1, 3]

max_val = tab[0]

for i in range(1, len(tab)):
    if tab[i] > max_val:
        max_val = tab[i]

print("Maksymalna wartość w tablicy:", max_val)
