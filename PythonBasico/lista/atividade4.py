print("Entre com números positivos:")
lista = []

while True:
    num = int(input())
    if num <= 0:
        break
    lista.append(num)

x = int(input("Número para procurar: "))

if x in lista:
    print(x, "pertence à lista.")
else:
    print(x, "não pertence à lista")