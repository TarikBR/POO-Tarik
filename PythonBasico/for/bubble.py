lista = [10, 5, 8, 11, 25, 3, 2]
print(lista)

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j + 1], lista[j] = lista[j], lista[j + 1]
        else:
            continue

print(lista)
