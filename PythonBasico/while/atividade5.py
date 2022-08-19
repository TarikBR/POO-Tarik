num = int(input("Insira um número para gerar a tabuada: "))
i = 1

print(f"Tabuada de {num}:")
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1