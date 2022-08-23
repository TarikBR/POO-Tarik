lista = [int(input("Digite um número: ")) for i in range(int(input("Quantos números serão lidos? ")))]
x = int(input("Número para procurar: "))
if x in lista:
    print(x, "pertence à lista.")
else:
    print(x, "não pertence à lista.")