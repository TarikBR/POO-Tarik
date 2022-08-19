i = 0
maior = 0
soma = 0

while i < 5:
    num = int(input("Digite um número: "))
    soma += num
    if num > maior:
        maior = num
    i += 1

print("\n")
print(f"O maior número é: {maior}")
print(f"A soma de todos os números é: {soma}")
print(f"A média dos números é: {soma / 5}")