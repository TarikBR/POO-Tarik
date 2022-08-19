num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0

if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux

num1 += 1
while num1 < num2:
    print(num1)
    soma += num1
    num1 += 1

print(f"\nA soma total dos números é: {soma}")